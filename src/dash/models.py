__all__ = ('DashboardSettings', 'DashboardWorkspace', 'DashboardEntry', 'DashboardPlugin')

import logging
logger = logging.getLogger(__name__)

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

from autoslug import AutoSlugField

from dash.base import plugin_registry, get_registered_plugins, get_registered_layouts
from dash.helpers import slugify_workspace
from dash.fields import OrderField

class DashboardSettings(models.Model):
    """
    Dashboard settings.

    :Properties:
        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `layout_uid` (str): Users' preferred layout.
        - `title` (str): Dashboard title.
        - `is_public` (bool): If set to True, available as public (read-only mode).
    """
    user = models.ForeignKey(User, verbose_name=_("User"), unique=True)
    layout_uid = models.CharField(_("Layout"), max_length=25, choices=get_registered_layouts())
    title = models.CharField(_("Title"), max_length=255)
    is_public = models.BooleanField(_("Is public?"), default=False, \
                                    help_text=_("Makes your dashboard to be visible to the public. Visibility "
                                                "of workspaces could be adjust separately for each workspace, "
                                                "however setting your dashboard to be visible to public, makes "
                                                "your default workspace visible to public too."))


class DashboardWorkspace(models.Model):
    """
    Dashboard workspace.

    :Properties:
        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `layout_uid` (str): Layout to which the entry belongs to.
        - `name` (str): Dashboard name.
        - `slug` (str): Dashboard slug.
        - `position` (int): Dashboard position.
    """
    user = models.ForeignKey(User, verbose_name=_("User"))
    layout_uid = models.CharField(_("Layout"), max_length=25, choices=get_registered_layouts())
    name = models.CharField(_("Name"), max_length=255)
    slug = AutoSlugField(populate_from='name', verbose_name=_("Slug"), unique=True, slugify=slugify_workspace)
    position = OrderField(_("Position"), null=True, blank=True)
    is_public = models.BooleanField(_("Is public?"), default=False, \
                                    help_text=_("Makes your workspace to be visible to the public."))

    class Meta:
        verbose_name = _("Dashboard workspace")
        verbose_name_plural = _("Dashboard workspaces")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __unicode__(self):
        return self.name

    def get_entries(self, user):
        """
        Gets all dashboard entries for user given.

        :param django.contrib.auth.models.User user:
        :return iterable:
        """
        return DashboardEntry._default_manager.get_for_workspace(
            user = self.user,
            layout_uid = self.layout_uid,
            workspace = self.slug
            )

    def get_absolute_url(self):
        """
        Absolute URL, which goes to the dashboard workspace page.

        :return string:
        """
        return reverse('dash.dashboard', kwargs={'workspace': self.slug})


class DashboardEntryManager(models.Manager):
    """
    Manager for ``dash.models.DashboardEntry``.
    """
    def get_for_user(self, user, layout_uid, workspace=None):
        """
        Gets all dashboard entries for user given.

        :param django.contrib.auth.models.User user:
        :param string layout_uid:
        :param string workspace: Workspace slug (``dash.models.DashboardWorkspace``).
        :return iterable:
        """
        return self.filter(user=user, layout_uid=layout_uid, workspace__slug=workspace)


class DashboardEntry(models.Model):
    """
    Dashboard entry (widget).

    Since workspace can be nullable (default), we duplicate the `layout_uid`.

    :Properties:
        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `workspace` (dash.models.DashboardWorkspace): Workspace to which the plugin belongs to.
          If left blank, entry belongs to default workspace.
        - `layout_uid` (str): Layout to which the entry belongs to.
        - `placeholder_uid` (str): Placeholder to which the entry belongs to.
        - `plugin_uid` (str): Plugin name.
        - `plugin_data` (str): JSON formatted string with plugin data.
        - `position` (int): Entry position.
    """
    user = models.ForeignKey(User, verbose_name=_("User"))
    workspace = models.ForeignKey(DashboardWorkspace, verbose_name=_("Workspace"), null=True, blank=True)
    layout_uid = models.CharField(_("Layout"), max_length=25, choices=get_registered_layouts())
    placeholder_uid = models.CharField(_("Placeholder"), max_length=255)
    plugin_uid = models.CharField(_("Plugin name"), max_length=255, choices=get_registered_plugins())
    plugin_data = models.TextField(verbose_name=_("Plugin data"), null=True, blank=True)
    position = models.PositiveIntegerField(_("Position"), null=True, blank=True)

    objects = DashboardEntryManager()

    class Meta:
        verbose_name = _("Dashboard entry")
        verbose_name_plural = _("Dashboard entries")

    def __unicode__(self):
        return "{0} plugin for user {1}".format(self.plugin_uid, self.user)

    def get_plugin(self, fetch_related_data=False, request=None):
        """
        Gets the plugin class (by ``plugin_name`` property), makes an instance of it, serves the
        data stored in ``plugin_data`` field (if available). Once all is done, plugin is ready to
        be rendered.

        :param bool fetch_related_data: When set to True, plugin is told to re-fetch all related
            data (stored in models or other sources).
        :return dash.base.DashboardPlugin: Subclass of ``dash.base.DashboardPlugin``.
        """
        # Getting plugin from registry.
        cls = plugin_registry.get(self.plugin_uid)

        # Creating plugin instance.
        plugin = cls(
            self.layout_uid,
            self.placeholder_uid,
            workspace = self.workspace,
            user = self.user,
            position = self.position
            )

        # So that plugin has the request object
        plugin.request = request

        return plugin.process(self.plugin_data, fetch_related_data=fetch_related_data)

    def plugin_uid_code(self):
        """
        Mainly used in admin.
        """
        # TODO - shall be showing the dimensions.
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

class DashboardPluginManager(models.Manager):
    """
    Manager for ``dash.models.DashboardPlugin``.
    """


class DashboardPlugin(models.Model):
    """
    Dashboard plugin. Used when ``dash.settings.RESTRICT_PLUGIN_ACCESS`` is set to True.

    :Properties:
        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users allowed to use the dashboard plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the user groups allowed to use the dashboard
          plugin.
    """
    plugin_uid = models.CharField(_("Plugin UID"), max_length=255, choices=get_registered_plugins(), \
                                   unique=True, editable=False)
    users = models.ManyToManyField(User, verbose_name=_("User"), null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_("Group"), null=True, blank=True)

    objects = DashboardPluginManager()

    class Meta:
        verbose_name = _("Dashboard plugin")
        verbose_name_plural = _("Dashboard plugins")

    def plugin_uid_code(self):
        """
        Mainly used in admin.
        """
        # TODO - shall be showing the dimensions.
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_uid_admin(self):
        """
        Mainly used in admin.
        """
        # TODO - shall be showing the dimensions.
        return "{0} ({1})".format(dict(get_registered_plugins()).get(self.plugin_uid, ''), self.plugin_uid)
    plugin_uid_admin.allow_tags = True
    plugin_uid_admin.short_description = _('Plugin')

    def groups_list(self):
        """
        Flat list (comma separated string) of groups allowed to use the dashboard plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([g.name for g in self.groups.all()])
    groups_list.allow_tags = True
    groups_list.short_description = _('Groups')

    def users_list(self):
        """
        Flat list (comma separated string) of users allowed to use the dashboard plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([u.username for u in self.users.all()])
    users_list.allow_tags = True
    users_list.short_description = _('Users')
