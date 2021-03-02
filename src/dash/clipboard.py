from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from .base import validate_placeholder_uid
from .helpers import (
    clone_plugin_data,
    lists_overlap,
    safe_text
)
from .models import (
    DashboardEntry,
    DashboardWorkspace
)
from .settings import PLUGIN_CLIPBOARD_KEY
from .utils import (
    build_cells_matrix,
    get_occupied_cells,
    get_user_plugin_uids
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'can_paste_entry_from_clipboard',
    'clear_clipboard_data',
    'copy_entry_to_clipboard',
    'cut_entry_to_clipboard',
    'get_plugin_data_from_clipboard',
    'make_session_key',
    'paste_entry_from_clipboard',
    'save_plugin_data_to_clipboard',
)


def make_session_key(layout_uid):
    """Make a session key based on the layout UID.

    :param str layout_uid:
    :return str:
    """
    return "{0}_{1}".format(PLUGIN_CLIPBOARD_KEY, layout_uid)


def save_plugin_data_to_clipboard(request,
                                  layout_uid,
                                  plugin_uid,
                                  plugin_data):
    """Save plugin to clipboard for later pasting.

    :param django.http.HttpRequest request:
    :param str layout_uid:
    :param str plugin_uid:
    :param str plugin_data: JSON data (stringified).
    :return bool: True on success. False otherwise.
    """
    request.session[make_session_key(layout_uid)] = {
        'plugin_uid': plugin_uid,
        'plugin_data': plugin_data
    }
    return True


def get_plugin_data_from_clipboard(request, layout_uid):
    """Retrieve the plugin clipboard.

    Note, that only last element is being saved.

    :param django.http.HttpRequest request:
    :param str layout_uid:
    :return dict:
    """
    session_key = make_session_key(layout_uid)
    if session_key in request.session:
        return request.session[session_key]


def clear_clipboard_data(request, layout_uid):
    """Clear the clipboard data."""
    session_key = make_session_key(layout_uid)
    if session_key in request.session:
        request.session[session_key] = None


def cut_entry_to_clipboard(request,
                           dashboard_entry,
                           delete_original_entry=True,
                           clone_data=True):
    """Cut ``dash.models.DashboardEntry`` to clipboard.

    :param django.http.HttpRequest request:
    :param dash.models.DashboardEntry dashboard_entry:
    :param bool delete_original_entry: If set to True, original entry is
        deleted; kept otherwise.
    :param bool clone_data: If set to Ture, plugin data is cloned.
    :return bool: True on success. False otherwise.
    """
    layout_uid = dashboard_entry.layout_uid
    plugin_uid = dashboard_entry.plugin_uid

    if clone_data:
        # plugin = dashboard_entry.get_plugin(request=request)

        # Getting cloned plugin data
        # plugin_data = plugin._clone_plugin_data(dashboard_entry)
        plugin_data = clone_plugin_data(dashboard_entry, request=request)

        # If none returned, using the still the current one (not cloned, which
        # is dangerous). Possible TODO for later.
        if plugin_data is None:
            plugin_data = dashboard_entry.plugin_data
    else:
        plugin_data = dashboard_entry.plugin_data

    save_plugin_data_to_clipboard(
        request=request,
        layout_uid=layout_uid,
        plugin_uid=plugin_uid,
        plugin_data=plugin_data
    )

    if delete_original_entry:
        dashboard_entry.delete()

    return True


def copy_entry_to_clipboard(request, dashboard_entry):
    """Copy ``dash.models.DashboardEntry`` to clipboard.

    :param django.http.HttpRequest request:
    :param dash.models.DashboardEntry dashboard_entry:
    :return bool: True on success. False otherwise.
    """
    return cut_entry_to_clipboard(
        request,
        dashboard_entry,
        delete_original_entry=False
    )


def paste_entry_from_clipboard(request,
                               layout,
                               placeholder_uid,
                               position,
                               workspace=None,
                               entries=[],
                               check_only=False,
                               clear_clipboard=True):
    """Paste entry from clipboard

    Paste entry from clipboard to the given placeholder of a workspace
    selected.

    :param django.http.HttpRequest request:
    :param str layout: Layout UID.
    :param str placeholder_uid: Placeholder UID.
    :param int position: Position.
    :param mixed workspace: Either str or ``dash.models.DashboardWorkspace``
        instance. If str is given, a database hit occurs in order to obtain
        the ``dash.models.DashboardWorkspace`` instance. Thus, if you have the
        workspace instance already, provide it as is, in order to minify
        database hits.
    :param iterable entries: If given, entries are not fetched but the
        existing iterable is used. Each item in the iterable should be an
        instance of ``dash.models.DashboardEntry``.
    :param bool check_only: If set to True, it's only checked if it's possible
        to paste from clipboard (the ``dashboard_entry.save()`` part is
        skipped, which means that the entry is not saved in the database).
    :return tuple (str, bool): (Plugin name, boolean True) tuple on success
        and (error message, boolean False) on failure.
    """
    clipboard_plugin_data = get_plugin_data_from_clipboard(request, layout.uid)
    if not clipboard_plugin_data:
        return _("Clipboard is empty!"), False

    if not validate_placeholder_uid(layout, placeholder_uid):
        return _("Invalid placeholder `{0}`.").format(placeholder_uid), False

    user_plugin_uids = get_user_plugin_uids(request.user)

    if isinstance(workspace, DashboardWorkspace):
        workspace_obj = workspace
    else:
        if workspace:
            try:
                workspace_obj = DashboardWorkspace._default_manager \
                                                  .get(slug=workspace)
            except ObjectDoesNotExist as e:
                workspace_obj = None
        else:
            workspace_obj = None

    dashboard_entry = DashboardEntry(
        user=request.user,
        workspace=workspace_obj,
        layout_uid=layout.uid,
        placeholder_uid=placeholder_uid,
        plugin_uid=clipboard_plugin_data['plugin_uid'],
        plugin_data=clipboard_plugin_data['plugin_data'],
        position=position
    )

    # We should now check if we have a space for pasting the plugin. For that
    # we should get the plugin and see if there's a space available for
    # the (workspace, placeholder, user) triple given.

    # Get the plugin.
    plugin = dashboard_entry.get_plugin()

    if plugin.uid not in user_plugin_uids:
        return (_("You're not allowed to "
                  "use the {0} plugin.".format(safe_text(plugin.name))), False)

    # Getting occupied cells
    placeholder = layout.get_placeholder(placeholder_uid)
    occupied_cells = build_cells_matrix(
        request.user,
        layout,
        placeholder,
        workspace=workspace
    )

    # Get cells occupied by plugin widget.
    widget_occupied_cells = get_occupied_cells(
        layout,
        placeholder,
        plugin.uid,
        position,
        check_boundaries=True
    )

    if widget_occupied_cells is not False \
       and not lists_overlap(widget_occupied_cells, occupied_cells):

        try:
            if not check_only:
                # Save data
                dashboard_entry.save()

                # Clear the clipboard
                clear_clipboard_data(request, layout.uid)

            return plugin.uid, True
        except Exception as err:
            return str(err), False


def can_paste_entry_from_clipboard(request,
                                   layout,
                                   placeholder_uid,
                                   position,
                                   workspace=None,
                                   entries=[]):
    """Check if clipboard plugin can be pasted into the placeholder.

    For actually pasting the plugin from clipboard into the placeholder, use
    ``dash.clipboard.paste_from_clipboard`` function.

    :param django.http.HttpRequest request:
    :param str layout:
    :param str placeholder_uid: Placeholder UID.
    :param int position:
    :param mixed workspace: Either str or ``dash.models.DashboardWorkspace``
        instance. If str is given, a database hit occurs in order to obtain
        the ``dash.models.DashboardWorkspace`` instance. Thus, if you have the
        workspace instance already, provide it as is, in order to minify
        database hits.
    :param iterable entries: If given, entries are not fetched but the existing
        iterable is used. Each item in the iterable should be an instance
        of ``dash.models.DashboardEntry``.
    :return tuple (str, bool): (Plugin name, boolean True) tuple on success
        and (error message, boolean False) on failure.
    """
    return paste_entry_from_clipboard(
        request=request,
        layout=layout,
        placeholder_uid=placeholder_uid,
        position=position,
        workspace=workspace,
        entries=entries,
        check_only=True
    )
