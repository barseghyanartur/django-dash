import logging

from autoslug import AutoSlugField

from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .base import (
    # get_registered_layouts,
    get_registered_plugins,
    plugin_registry,
)
from .helpers import slugify_workspace
from .fields import OrderField

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'DashboardEntry',
    'DashboardEntryManager',
    'DashboardPlugin',
    'DashboardPluginManager',
    'DashboardSettings',
    'DashboardWorkspace',
)

AUTH_USER_MODEL = settings.AUTH_USER_MODEL
logger = logging.getLogger(__name__)


class DashboardSettings(models.Model):
    """Dashboard settings.

    :Properties:
        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `layout_uid` (str): Users' preferred layout.
        - `title` (str): Dashboard title.
        - `is_public` (bool): If set to True, available as public (read-only
          mode).
    """

    user = models.OneToOneField(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    layout_uid = models.CharField(_("Layout"), max_length=25)
    title = models.CharField(_("Title"), max_length=255)
    allow_different_layouts = models.BooleanField(
        _("Allow different layouts per workspace?"),
        default=False,
        help_text=_("Allows you to use different layouts for each workspace.")
    )
    is_public = models.BooleanField(
        _("Is public?"),
        default=False,
        help_text=_("Makes your dashboard to be visible to the public. "
                    "Visibility of workspaces could be adjust separately "
                    "for each workspace, however setting your dashboard to be "
                    "visible to public, makes your default workspace "
                    "visible to public too.")
    )

    class Meta:
        """Meta."""

        verbose_name = _("Dashboard settings")
        verbose_name_plural = _("Dashboard settings")

    def __str__(self):
        return self.title


class DashboardWorkspace(models.Model):
    """Dashboard workspace.

    :Properties:

        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `layout_uid` (str): Layout to which the entry belongs to.
        - `name` (str): Dashboard name.
        - `slug` (str): Dashboard slug.
        - `position` (int): Dashboard position.
        - `is_public` (int): If set to True, is visible to public.
        - `is_cloneable` (bool): If set to True, is cloneable.
        - `shared_with` (django.db.models.ManyToManyField): Users the workspace
          shared with. If workspace is shared with specific user, then the
          user it's shared with can also clone the workspace.
    """
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    layout_uid = models.CharField(_("Layout"), max_length=25)
    name = models.CharField(_("Name"), max_length=255)
    slug = AutoSlugField(populate_from='name', verbose_name=_("Slug"),
                         unique=True, slugify=slugify_workspace)
    position = OrderField(_("Position"), null=True, blank=True)
    is_public = models.BooleanField(
        _("Is public?"),
        default=False,
        help_text=_("Makes your workspace to be visible to the public.")
    )
    is_cloneable = models.BooleanField(
        _("Is cloneable?"),
        default=False,
        help_text=_("Makes your workspace to be cloneable by other users.")
    )

    class Meta:
        """Meta."""

        verbose_name = _("Dashboard workspace")
        verbose_name_plural = _("Dashboard workspaces")
        unique_together = (('user', 'slug'), ('user', 'name'),)

    def __str__(self):
        return self.name

    @property
    def is_clonable(self):
        """For backwards compatibility."""
        return self.is_cloneable

    def get_entries(self, user):
        """Get all dashboard entries for user given.

        :param django.contrib.auth.models.User user:
        :return iterable:
        """
        return DashboardEntry._default_manager.get_for_workspace(
            user=self.user,
            layout_uid=self.layout_uid,
            workspace=self.slug
        )

    def get_absolute_url(self):
        """Absolute URL, which goes to the dashboard workspace page.

        :return string:
        """
        return reverse('dash.dashboard', kwargs={'workspace': self.slug})


class DashboardEntryManager(models.Manager):
    """Manager for ``dash.models.DashboardEntry``."""

    def get_for_user(self, user, layout_uid, workspace=None):
        """Get all dashboard entries for user given.

        :param django.contrib.auth.models.User user:
        :param string layout_uid:
        :param string workspace: Workspace slug
            (``dash.models.DashboardWorkspace``).
        :return iterable:
        """
        return self.filter(
            user=user,
            layout_uid=layout_uid,
            workspace__slug=workspace
        )


class DashboardEntry(models.Model):
    """Dashboard entry (widget).

    Since workspace can be nullable (default), we duplicate the `layout_uid`.

    :Properties:

        - `user` (django.contrib.auth.models.User: User owning the plugin.
        - `workspace` (dash.models.DashboardWorkspace): Workspace to which the
          plugin belongs to. If left blank, entry belongs to default workspace.
        - `layout_uid` (str): Layout to which the entry belongs to.
        - `placeholder_uid` (str): Placeholder to which the entry belongs to.
        - `plugin_uid` (str): Plugin name.
        - `plugin_data` (str): JSON formatted string with plugin data.
        - `position` (int): Entry position.
    """
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    workspace = models.ForeignKey(
        DashboardWorkspace,
        null=True,
        blank=True,
        verbose_name=_("Workspace"),
        on_delete=models.CASCADE,

    )
    layout_uid = models.CharField(_("Layout"), max_length=25)
    placeholder_uid = models.CharField(_("Placeholder"), max_length=255)
    plugin_uid = models.CharField(_("Plugin name"), max_length=255)
    plugin_data = models.TextField(verbose_name=_("Plugin data"), null=True,
                                   blank=True)
    position = models.PositiveIntegerField(_("Position"), null=True,
                                           blank=True)

    objects = DashboardEntryManager()

    class Meta:
        """Meta."""

        verbose_name = _("Dashboard entry")
        verbose_name_plural = _("Dashboard entries")

    def __str__(self):
        return "{0} plugin for user {1}".format(self.plugin_uid, self.user)

    def get_plugin(self, fetch_related_data=False, request=None):
        """Get the plugin class.

        Get the plugin class (by ``plugin_uid`` property), makes an instance
        of it, serves the data stored in ``plugin_data`` field (if available).
        Once all is done, plugin is ready to be rendered.

        :param bool fetch_related_data: When set to True, plugin is told to
            re-fetch all related data (stored in models or other sources).
        :return dash.base.DashboardPlugin: Subclass of
            ``dash.base.DashboardPlugin``.
        """
        # Getting plugin from registry.
        cls = plugin_registry.get(self.plugin_uid)

        if not cls:
            # No need to log here, since already logged in registry.
            return None

        # Creating plugin instance.
        plugin = cls(
            self.layout_uid,
            self.placeholder_uid,
            workspace=self.workspace,
            user=self.user,
            position=self.position
        )

        # So that plugin has the request object
        plugin.request = request

        return plugin.process(
            self.plugin_data,
            fetch_related_data=fetch_related_data
        )

    def plugin_uid_code(self):
        """Mainly used in admin."""
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')


class DashboardPluginManager(models.Manager):
    """Manager for ``dash.models.DashboardPlugin``."""


class DashboardPlugin(models.Model):
    """Dashboard plugin.

    Used when ``dash.settings.RESTRICT_PLUGIN_ACCESS`` is set to True.

    :Properties:

        - `plugin_uid` (str): Plugin UID.
        - `users` (django.contrib.auth.models.User): White list of the users
          allowed to use the dashboard plugin.
        - `groups` (django.contrib.auth.models.Group): White list of the user
          groups allowed to use the dashboard plugin.
    """

    plugin_uid = models.CharField(_("Plugin UID"), max_length=255,
                                  unique=True, editable=False)
    users = models.ManyToManyField(
        AUTH_USER_MODEL,
        verbose_name=_("User"),
        blank=True
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("Group"),
        blank=True
    )

    objects = DashboardPluginManager()

    class Meta:
        """Meta."""

        verbose_name = _("Dashboard plugin")
        verbose_name_plural = _("Dashboard plugins")

    def __str__(self):
        return "{0} ({1})".format(
            dict(get_registered_plugins()).get(self.plugin_uid, ''),
            self.plugin_uid
        )

    def plugin_uid_code(self):
        """Mainly used in admin."""
        return self.plugin_uid
    plugin_uid_code.allow_tags = True
    plugin_uid_code.short_description = _('UID')

    def plugin_uid_admin(self):
        """Mainly used in admin."""
        return self.__str__()
    plugin_uid_admin.allow_tags = True
    plugin_uid_admin.short_description = _('Plugin')

    def groups_list(self):
        """Flat groups list.

        Flat list (comma separated string) of groups allowed to use the
        dashboard plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([g.name for g in self.groups.all()])
    groups_list.allow_tags = True
    groups_list.short_description = _('Groups')

    def users_list(self):
        """Flat users list.

        Flat list (comma separated string) of users allowed to use the
        dashboard plugin. Used in Django admin.

        :return string:
        """
        return ', '.join([u.username for u in self.users.all()])
    users_list.allow_tags = True
    users_list.short_description = _('Users')
