__all__ = ('get_allowed_plugin_uids', 'get_user_plugins', 'get_user_plugin_uids', 'get_widgets', \
           'update_plugin_data', 'sync_plugins', 'get_workspaces', 'build_cells_matrix', \
           'get_or_create_dashboard_settings', 'get_dashboard_settings', 'get_public_dashboard_url')

from six import PY3

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_text

from dash.base import plugin_registry, get_registered_plugin_uids, ensure_autodiscover, get_registered_plugins
from dash.base import plugin_widget_registry, PluginWidgetRegistry, get_layout
from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder
from dash.models import DashboardEntry, DashboardPlugin, DashboardWorkspace, DashboardSettings
from dash.helpers import slugify_workspace, lists_overlap
from dash.exceptions import PluginWidgetOutOfPlaceholderBoundaries
from dash.settings import RESTRICT_PLUGIN_ACCESS, DEBUG

import logging
logger = logging.getLogger(__name__)

_ = lambda s: s

def get_allowed_plugin_uids(user):
    """
    Gets allowed plugins uids for user given.

    :param django.contrib.auth.models import User:
    :return list:
    """
    try:
        queryset_groups = DashboardPlugin._default_manager.filter(groups__in=user.groups.all()).distinct()
        queryset_users = DashboardPlugin._default_manager.filter(users=user).distinct()
        queryset = queryset_groups | queryset_users
        queryset = queryset.only('plugin_uid')
        return [p.plugin_uid for p in queryset]
    except Exception as e:
        if DEBUG:
            logger.debug(e)
        return []

def get_user_plugins(user):
    """
    Gets a list of user plugins in a form if tuple (plugin name, plugin description). If not yet autodiscovered,
    autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        return get_registered_plugins()

    registered_plugins = []

    allowed_plugin_uids = get_allowed_plugin_uids(user)

    for uid, plugin in plugin_registry._registry.items():
        if uid in allowed_plugin_uids:
            registered_plugins.append((uid, force_text(plugin.name)))

    return registered_plugins

def get_user_plugin_uids():
    """
    Gets a list of user plugin uids as a list . If not yet autodiscovered, autodiscovers them.

    :return list:
    """
    ensure_autodiscover()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        return get_registered_plugin_keys()

    registered_plugins = []

    allowed_plugin_uids = get_allowed_plugin_uids(user)

    for uid in plugin_registry._registry.items():
        if uid in allowed_plugin_uids:
            registered_plugins.append(uid)

    return registered_plugins

def get_widgets(layout, placeholder, user=None, workspace=None, position=None, occupied_cells=[]):
    """
    Gets widgets. In case if in restricted mode (``RESTRICT_PLUGIN_ACCESS`` is set to True),
    user argument should be provided. Based on it, the list of plugins is returned.  Restrictions are
    bypassed in case if ``RESTRICT_PLUGIN_ACCESS`` is set to False or user given is a superuser.

    Placeholders are validated already. We don't need to have validation here.

    :param dash.base.BaseDashLayout layout: Layout object.
    :param string placeholder_uid: Placeholder uid.
    :param django.contrib.auth.models.User user:
    :param string workspace: Workspace slug.
    :param int position: Plugin position.
    :param list occupied_cells: List of already occupied cells.
    :return list:
    """
    # We should get the layout, see loop through its' plugins and see which of those do have rendererrs. Then
    # we get all the plugins (based on whether they are restricted or not - get the list) and then filter
    # out those that do not have renderers.

    ensure_autodiscover()

    registered_widgets = {}

    plugin_widget_uids = plugin_widget_registry._registry.keys()

    if not RESTRICT_PLUGIN_ACCESS or getattr(user, 'is_superuser', False):
        for uid, plugin in plugin_registry._registry.items():
            # We should make sure that there are widgets available for the placeholder.
            plugin_widget_uid = PluginWidgetRegistry.namify(layout.uid, placeholder.uid, uid)

            # Get cells occupied by plugin widget.
            widget_occupied_cells = get_occupied_cells(layout, placeholder, uid, position, check_boundaries=True)

            if plugin_widget_uid in plugin_widget_uids and widget_occupied_cells is not False and \
               not lists_overlap(widget_occupied_cells, occupied_cells):
                plugin_widget = plugin_widget_registry.get(plugin_widget_uid)
                kwargs = {'placeholder_uid': placeholder.uid, 'plugin_uid': uid}
                if workspace:
                    kwargs.update({'workspace': workspace})
                if position:
                    kwargs.update({'position': position})

                plugin_group = force_text(plugin.group)
                if not plugin_group in registered_widgets:
                    registered_widgets[plugin_group] = []

                if PY3:
                    widget_name = force_text(plugin.name, encoding='utf-8')
                else:
                    widget_name = force_text(plugin.name, encoding='utf-8').encode('utf-8')

                registered_widgets[plugin_group].append((
                    uid,
                    '{0} ({1}x{2})'.format(widget_name, plugin_widget.cols, plugin_widget.rows),
                    reverse('dash.add_dashboard_entry', kwargs=kwargs)
                    ))
    else:
        allowed_plugin_uids = get_allowed_plugin_uids(user)

        for uid, plugin in plugin_registry._registry.items():
            # We should make sure that there are widgets available for the placeholder and user has access to the
            # widget desired.
            plugin_widget_uid = PluginWidgetRegistry.namify(layout.uid, placeholder.uid, uid)

            # Get cells occupied by plugin widget.
            widget_occupied_cells = get_occupied_cells(layout, placeholder, uid, position, check_boundaries=True)

            if uid in allowed_plugin_uids and plugin_widget_uid in plugin_widget_uids and \
               widget_occupied_cells is not False and not lists_overlap(widget_occupied_cells, occupied_cells):
                plugin_widget = plugin_widget_registry.get(plugin_widget_uid)
                kwargs = {'placeholder_uid': placeholder.uid, 'plugin_uid': uid}
                if workspace:
                    kwargs.update({'workspace': workspace})
                if position:
                    kwargs.update({'position': position})

                plugin_group = force_text(plugin.group)
                if not plugin_group in registered_widgets:
                    registered_widgets[plugin_group] = []

                registered_widgets[plugin_group].append(
                    (
                        uid,
                        '{0} ({1}x{2})'.format(force_text(plugin.name), plugin_widget.cols, plugin_widget.rows),
                        reverse('dash.add_dashboard_entry', kwargs=kwargs)
                    )
                    )

    return registered_widgets

def update_plugin_data():
    """
    Updates the plugin data for all dashboard entries of all users. Rules for update are specified in the
    plugin itself.
    """
    dashboard_entries = DashboardEntry._default_manager.all()

    for entry in dashboard_entries:
        entry.get_plugin().update_plugin_data(entry)

def sync_plugins():
    """
    Syncs the registered plugin list with data in ``dash.models.DashboardPlugin``.
    """
    # If not in restricted mode, the quit.

    if not RESTRICT_PLUGIN_ACCESS:
        return

    registered_plugins = set(get_registered_plugin_uids())

    synced_plugins = set([p.plugin_uid for p in DashboardPlugin._default_manager.only('plugin_uid')])

    non_synced_plugins = registered_plugins - synced_plugins

    if not non_synced_plugins:
        return

    buf = []

    for plugin_uid in non_synced_plugins:
        buf.append(DashboardPlugin(plugin_uid=plugin_uid))

    DashboardPlugin._default_manager.bulk_create(buf)

def get_workspaces(user, layout_uid=None, workspace=None, public=False):
    """
    Gets previous, current, next and and a queryset of all workspaces.

    :param string workspace:
    :param django.contrib.auth.models.User:
    :return dict:
    """
    # We need to show workspaces
    q_kwargs = {'user': user, 'layout_uid': layout_uid}
    if public:
        q_kwargs.update({'is_public': public})

    workspaces = list(DashboardWorkspace._default_manager.filter(**q_kwargs).only('id', 'name', 'slug') \
                                        .order_by('position')[:])

    next = None
    previous = None
    current = None
    current_not_found = False

    if workspace:

        # Slugifying the workspace
        workspace_slug = slugify_workspace(workspace)
        num_workspaces = len(workspaces)

        for index, ws in enumerate(workspaces):
            if workspace_slug == ws.slug:
                current = ws

                if 0 == index:
                    # No previous workspace (previous is default).
                    try:
                        next = workspaces[1]
                    except IndexError:
                        pass

                elif num_workspaces == index:
                    # No next workspace (next is default).
                    try:
                        previous = workspaces[index - 1]
                    except IndexError:
                        pass

                else:
                    # Getting previous and next workspaces.
                    try:
                        previous = workspaces[index - 1]
                    except IndexError:
                        pass

                    try:
                        next = workspaces[index + 1]
                    except IndexError:
                        pass

        if current is None:
            current_not_found = True

    else:
        try:
            previous = workspaces[-1]
        except IndexError as e:
            pass

        try:
            next = workspaces[0]
        except IndexError as e:
            pass

    return {
        'workspaces': workspaces,
        'next_workspace': next,
        'previous_workspace': previous,
        'current_workspace': current,
        'current_workspace_not_found': current_not_found
    }

def get_occupied_cells(layout, placeholder, plugin_uid, position, check_boundaries=False, fail_silently=True):
    """
    Get cells occupied by the given dashboard entry.

    :param dash.base.BaseDashboardLayout dashboard_entry: Instance of subclassed
        ``dash.base.BaseDashboardLayout`` object.
    :param dash.base.BaseDashboardPlaceholder placeholder: Instance of subclassed
        ``dash.base.BaseDashboardPlaceholder`` object.
    :param string plugin_uid: UID of the plugin to check against.
    :param int position: Position of the plugin to check against.
    :param bool check_boundaries: If set to True, boundaries of the placeholders are also considered.
    :param bool fail_silently: If set to True, no exceptions are raised.
    :return mixed: Returns a list (could be an empty list as well) if all goes well and returns boolean False
        if out of the placeholder boundaries.
    """
    assert isinstance(layout, BaseDashboardLayout)
    #assert issubclass(placeholder, BaseDashboardPlaceholder)

    widget_cls = plugin_widget_registry.get(
        PluginWidgetRegistry.namify(layout.uid, placeholder.uid, plugin_uid)
        )
    occupied_cells = []
    placeholder_max_cell_num = placeholder.cols * placeholder.rows

    try:
        position = int(position)
    except Exception as e:
        if fail_silently:
            return False
        else:
            raise e

    if widget_cls:

        # First check the basic things.
        if check_boundaries:
            # Checking if widget isn't touching the boundaries. Checking the widget width.
            relative_col_num = position % placeholder.cols
            if 0 == relative_col_num:
                relative_col_num = placeholder.cols

            if (relative_col_num + widget_cls.cols - 1) > placeholder.cols:
                if fail_silently:
                    return False
                else:
                    raise PluginWidgetOutOfPlaceholderBoundaries("Widget is out of placeholder boundaries.")

            # Checking if widget isn't touching the boundaries. Checking the widget height.
            #relative_row_num = position % placeholder.rows
            #if 0 == relative_row_num:
            #    relative_row_num = placeholder.rows
            #if (relative_row_num + widget_cls.rows - 1) > placeholder.rows:
            #    if fail_silently:
            #        return False
            #    else:
            #        raise PluginWidgetOutOfPlaceholderBoundaries("Widget is out of placeholder boundaries.")

        # Now check the collision with other plugin widgets.
        for row in range(0, widget_cls.rows):
            for col in range(0, widget_cls.cols):
                cell_num = position + col + (row * placeholder.cols)

                if check_boundaries and cell_num > placeholder_max_cell_num:
                    if fail_silently:
                        return False
                    else:
                        raise PluginWidgetOutOfPlaceholderBoundaries("Widget is out of placeholder boundaries.")
                occupied_cells.append(cell_num)

    return occupied_cells

def build_cells_matrix(user, layout, placeholder, workspace=None):
    """
    Builds the cells matrix.

    :param django.contrib.auth.models.User user:
    :param string placeholder_uid:
    :param string workspace: Workspace slug.
    :return list: List of cells occupied.
    """
    assert isinstance(layout, BaseDashboardLayout)
    assert issubclass(placeholder, BaseDashboardPlaceholder)

    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(user)
    user_plugin_uids = [uid for uid, repr in registered_plugins]

    # Getting the queryset for user and freezing it.
    dashboard_entries = DashboardEntry._default_manager \
                                      .get_for_user(user=user, layout_uid=layout.uid, workspace=workspace) \
                                      .select_related('workspace', 'user') \
                                      .filter(plugin_uid__in=user_plugin_uids) \
                                      .filter(placeholder_uid=placeholder.uid) \
                                      .order_by('placeholder_uid', 'position')[:]

    matrix = []
    for dashboard_entry in dashboard_entries:
        occupied_cells = get_occupied_cells(layout, placeholder, dashboard_entry.plugin_uid, dashboard_entry.position)
        if occupied_cells:
            matrix += occupied_cells
        # Now we should calculate how much space each widget occupies.

    return matrix

def get_or_create_dashboard_settings(user):
    """
    Gets dashboard settings for the user given. If no settings found, creates default settings.

    :param django.contrib.auth.models.User:
    :return dash.models.DashboardSettings: Returns ``dash.models.DashboardSettings`` instance.
    """
    # Check if user trying to edit the dashboard workspace actually owns it.
    try:
        dashboard_settings = DashboardSettings._default_manager.select_related('user').get(user=user)
    except ObjectDoesNotExist as e:
        layout = get_layout(as_instance=True)
        dashboard_settings = DashboardSettings()
        dashboard_settings.layout_uid = layout.uid
        dashboard_settings.user = user
        dashboard_settings.save()

    return dashboard_settings

def get_dashboard_settings(username):
    """
    Gets dashboard settings for the user given. If no settings found, creates default settings.

    :param string username:
    :return dash.models.DashboardSettings: Returns ``dash.models.DashboardSettings`` instance.
    """
    # Check if user trying to edit the dashboard workspace actually owns it.
    try:
        return DashboardSettings._default_manager.select_related('user').get(user__username=username)
    except ObjectDoesNotExist as e:
        pass

def get_public_dashboard_url(dashboard_settings):
    """
    Gets resolved public dashboard URL (if public dashboard app is installed == present in the global
    urls module of the project).

    :param dash.models.DashboardSettings: Instance of `dash.models.DashboardSettings`.
    :return string:
    """
    if dashboard_settings.is_public:
        try:
            # Resolve URL
            return reverse('dash.public_dashboard', kwargs={'username': dashboard_settings.user.username})
        except:
            # Most likely, the public dashboard is not present
            pass
    return ''

def clean_plugin_data(dashboard_entries, request=None):
    """
    Cleans up the plugin data (database, files) for the dashboard_entries given.

    :param iterable dashboard_entries:
    :param django.http.HttpRequest request:
    :return bool: Boolean True if no errors occured and False otherwise.
    """
    errors = False
    for dashboard_entry in dashboard_entries:
        plugin = dashboard_entry.get_plugin(request=request)
        try:
            plugin.delete_plugin_data()
        except Exception as e:
            errors = True
            logger.debug(str(e))

    return not errors
