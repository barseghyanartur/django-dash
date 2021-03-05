import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext, gettext_lazy as _

from .base import (
    get_layout,
    plugin_registry,
    # plugin_widget_registry,
    # PluginWidgetRegistry,
    validate_placeholder_uid,
    validate_plugin_uid,
)
from .clipboard import (
    can_paste_entry_from_clipboard,
    copy_entry_to_clipboard,
    cut_entry_to_clipboard,
    get_plugin_data_from_clipboard,
    paste_entry_from_clipboard,
)
from .decorators import (
    edit_dashboard_permission_required,
    permissions_required,
    SATISFY_ALL,
    use_clipboard_permission_required,
)
from .forms import DashboardWorkspaceForm, DashboardSettingsForm
from .helpers import (
    clean_plugin_data,
    iterable_to_dict,
    lists_overlap,
    safe_text,
    slugify_workspace,
)
from .models import DashboardEntry, DashboardWorkspace
from .settings import RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT
from .utils import (
    build_cells_matrix,
    clone_workspace,
    get_occupied_cells,
    get_or_create_dashboard_settings,
    get_public_dashboard_url,
    get_user_plugins,
    get_widgets,
    get_workspaces,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'add_dashboard_entry',
    'clone_dashboard_workspace',
    'copy_dashboard_entry',
    'create_dashboard_workspace',
    'cut_dashboard_entry',
    'dashboard',
    'dashboard_workspaces',
    'delete_dashboard_entry',
    'delete_dashboard_workspace',
    'edit_dashboard',
    'edit_dashboard_entry',
    'edit_dashboard_settings',
    'edit_dashboard_workspace',
    'paste_dashboard_entry',
    'plugin_widgets',
)

# ***************************************************************************
# ***************************************************************************
# **************************** Dashboard views ******************************
# ***************************************************************************
# ***************************************************************************


@login_required
def dashboard(request, workspace=None):
    """Dashboard.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug. If given, the workspace loaded.
        Otherwise we deal with no workspace.
    :return django.http.HttpResponse:
    """
    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(request.user)
    user_plugin_uids = [uid for uid, repr in registered_plugins]

    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    workspaces = get_workspaces(
        request.user,
        dashboard_settings.layout_uid,
        workspace,
        different_layouts=dashboard_settings.allow_different_layouts,
    )

    layout = get_layout(
        layout_uid=(
            workspaces['current_workspace'].layout_uid
            if workspaces['current_workspace']
            else dashboard_settings.layout_uid
        ),
        as_instance=True
    )

    # If workspace with slug given is not found in the list of workspaces
    # redirect to the default dashboard.
    if workspaces['current_workspace_not_found']:
        msg = _('The workspace with slug "{0}" does '
                'not belong to layout "{1}".').format(workspace, layout.name)
        if dashboard_settings.allow_different_layouts:
            msg = _('The workspace with slug "{0}" does not exist').format(
                workspace
            )
        messages.info(request, msg)
        return redirect('dash.edit_dashboard')

    # Getting the (frozen) queryset.
    dashboard_entries = DashboardEntry._default_manager.get_for_user(
        user=request.user,
        layout_uid=layout.uid,
        workspace=workspace
    ).select_related(
        'workspace',
        'user'
    ).filter(
        plugin_uid__in=user_plugin_uids
    ).order_by(
        'placeholder_uid',
        'position'
    )[:]

    placeholders = layout.get_placeholder_instances(
        dashboard_entries, request=request
    )

    layout.collect_widget_media(dashboard_entries)

    context = {
        'placeholders': placeholders,
        'placeholders_dict': iterable_to_dict(
            placeholders,
            key_attr_name='uid'
        ),
        'css': layout.get_css(placeholders),
        'layout': layout,
        'dashboard_settings': dashboard_settings,
    }

    context.update(workspaces)

    context.update(
        {'public_dashboard_url': get_public_dashboard_url(dashboard_settings)}
    )

    template_name = layout.get_view_template_name(request)

    return render(request, template_name, context)


@login_required
@edit_dashboard_permission_required()
def edit_dashboard(request, workspace=None):
    """Edit dashboard.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug. If given, the workspace loaded.
        Otherwise we deal with no workspace.
    :return django.http.HttpResponse:
    """
    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(request.user)
    user_plugin_uids = [uid for uid, _repr in registered_plugins]

    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    workspaces = get_workspaces(
        request.user,
        dashboard_settings.layout_uid,
        workspace,
        different_layouts=dashboard_settings.allow_different_layouts
    )

    layout = get_layout(
        layout_uid=(
            workspaces['current_workspace'].layout_uid
            if workspaces['current_workspace']
            else dashboard_settings.layout_uid
        ),
        as_instance=True
    )

    # If workspace with slug given is not found in the list of workspaces
    # redirect to the default dashboard.
    if workspaces['current_workspace_not_found']:
        messages.info(
            request,
            _('The workspace with slug "{0}" does '
              'not belong to layout "{1}".').format(workspace, layout.name)
            )
        return redirect('dash.edit_dashboard')

    # Getting the (frozen) queryset.
    dashboard_entries = DashboardEntry._default_manager.get_for_user(
        user=request.user,
        layout_uid=layout.uid,
        workspace=workspace
    ).select_related(
        'workspace',
        'user'
    ).filter(
        plugin_uid__in=user_plugin_uids
    ).order_by(
        'placeholder_uid',
        'position'
    )[:]

    placeholders = layout.get_placeholder_instances(
        dashboard_entries,
        workspace=workspace,
        request=request
    )

    layout.collect_widget_media(dashboard_entries)

    context = {
        'placeholders': placeholders,
        'placeholders_dict': iterable_to_dict(
            placeholders,
            key_attr_name='uid'
        ),
        'css': layout.get_css(placeholders),
        'layout': layout,
        'edit_mode': True,
        'dashboard_settings': dashboard_settings,
    }

    context.update(workspaces)

    context.update(
        {'public_dashboard_url': get_public_dashboard_url(dashboard_settings)}
    )

    template_name = layout.get_edit_template_name(request)

    return render(request, template_name, context)


# ***************************************************************************
# ***************************************************************************
# ********************* Add/edit/delete dashboard entry *********************
# ***************************************************************************
# ***************************************************************************


@login_required
@permission_required('dash.add_dashboardentry')
def add_dashboard_entry(
    request,
    placeholder_uid,
    plugin_uid,
    workspace=None,
    position=None,
    template_name='dash/add_dashboard_entry.html',
    template_name_ajax='dash/add_dashboard_entry_ajax.html'
):
    """Add dashboard entry.

    :param django.http.HttpRequest request:
    :param string placeholder_uid: Placeholder UID.
    :param string plugin_uid: Plugin UID.
    :param string workspace: Workspace slug.
    :param int position: If given, provided as position for the
        plugin (conflict resolution should take place).
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    workspace_obj = None
    if workspace:
        workspace_slug = slugify_workspace(workspace)
        filters = {
            'slug': workspace_slug,
            'user': request.user,
        }
        if not dashboard_settings.allow_different_layouts:
            filters.update({
                'layout_uid': dashboard_settings.layout_uid,
            })
        try:
            workspace_obj = DashboardWorkspace._default_manager.get(**filters)
        except ObjectDoesNotExist as e:
            if dashboard_settings.allow_different_layouts:
                message = _('The workspace with slug "{0}" was not found.'
                            '').format(workspace_slug)
            else:
                message = _(
                    'The workspace with slug "{0}" does not belong to '
                    'layout "{1}".'
                ).format(workspace_slug, get_layout(as_instance=True).name)
            messages.info(request, message)
            return redirect('dash.edit_dashboard')

    if dashboard_settings.allow_different_layouts and workspace_obj:
        layout_uid = workspace_obj.layout_uid
    else:
        layout_uid = dashboard_settings.layout_uid

    layout = get_layout(layout_uid=layout_uid, as_instance=True)

    if not validate_placeholder_uid(layout, placeholder_uid):
        raise Http404(
            gettext("Invalid placeholder: {0}").format(placeholder_uid)
        )

    if not validate_plugin_uid(plugin_uid):
        raise Http404(gettext("Invalid plugin name: {0}").format(plugin_uid))

    placeholder = layout.get_placeholder(placeholder_uid)

    # Cell that would be occupied by the plugin upon addition.
    widget_occupied_cells = get_occupied_cells(
        layout,
        placeholder,
        plugin_uid,
        position,
        check_boundaries=True,
        fail_silently=True
    )

    # Cells currently occupied in the workspace given.
    occupied_cells = build_cells_matrix(
        request.user,
        layout,
        placeholder,
        workspace
    )

    # Checking if it's still possible to insert a widget.
    if widget_occupied_cells is False \
       or lists_overlap(widget_occupied_cells, occupied_cells):

        raise Http404(gettext("Collisions detected"))

    plugin = plugin_registry.get(plugin_uid)(layout.uid, placeholder_uid)
    plugin.request = request

    if plugin.add_form_template:
        template_name = plugin.add_form_template

    # Template context
    context = {
        'layout': layout,
        'dashboard_settings': dashboard_settings,
    }

    obj = DashboardEntry()
    obj.layout_uid = layout.uid
    obj.placeholder_uid = placeholder_uid
    obj.plugin_uid = plugin_uid
    obj.user = request.user
    obj.workspace = workspace_obj

    # If plugin has form, it is configurable which means we have to load the
    # plugin form and validate user input.
    plugin_form = plugin.get_form()
    if plugin_form:
        # If POST request and form data is valid, save the data and redirect
        # to the dashboard edit.
        if request.method == 'POST':
            form = plugin.get_initialised_create_form_or_404(
                data=request.POST, files=request.FILES
            )
            if form.is_valid():
                # Saving the plugin form data.
                form.save_plugin_data(request=request)

                # Getting the plugin data.
                obj.plugin_data = form.get_plugin_data(request=request)

                # If position given, use it.
                try:
                    position = int(position)
                except Exception:
                    position = None

                if position:
                    obj.position = position

                # Save the object.
                obj.save()

                messages.info(
                    request,
                    _('The dashboard widget "{0}" was added successfully.'
                      '').format(plugin.name)
                )

                # Redirect to the dashboard view.
                if obj.workspace:
                    return redirect(
                        'dash.edit_dashboard', workspace=obj.workspace.slug
                    )
                else:
                    return redirect('dash.edit_dashboard')

        # If POST but data invalid, show the form with errors.
        else:
            form = plugin.get_initialised_create_form_or_404()

        context.update(
            {'form': form, 'plugin_uid': plugin_uid, 'plugin': plugin}
        )

    # If plugin is not configurable, it's just saved as is.
    else:
        obj.save()
        return redirect('dash.edit_dashboard')

    if layout.add_dashboard_entry_ajax_template_name:
        template_name_ajax = layout.add_dashboard_entry_ajax_template_name

    context.update(
        {'add_dashboard_entry_ajax_template_name': template_name_ajax}
    )

    if request.is_ajax():
        template_name = template_name_ajax
    elif layout.add_dashboard_entry_template_name:
        template_name = layout.add_dashboard_entry_template_name

    return render(request, template_name, context)


@login_required
@permission_required('dash.change_dashboardentry')
def edit_dashboard_entry(
    request,
    entry_id,
    template_name='dash/edit_dashboard_entry.html',
    template_name_ajax='dash/edit_dashboard_entry_ajax.html'
):
    """Edit dashboard entry.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the dashboard entry to edit.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    try:
        obj = DashboardEntry._default_manager.select_related(
            'workspace'
        ).get(
            pk=entry_id,
            user=request.user
        )
    except ObjectDoesNotExist as err:
        raise Http404(err)

    if obj.layout_uid:
        layout_uid = obj.layout_uid
    else:
        layout_uid = dashboard_settings.layout_uid

    layout = get_layout(layout_uid=layout_uid, as_instance=True)

    plugin = obj.get_plugin(fetch_related_data=True)
    plugin.request = request

    if plugin.edit_form_template:
        template_name = plugin.edit_form_template

    # Template context
    context = {
        'layout': layout,
        'dashboard_settings': dashboard_settings,
    }

    # If plugin has form, it is configurable which means we have to load the
    # plugin form and validate user input.
    plugin_form = plugin.get_form()
    if plugin_form:
        # If POST request and form data is valid, save the data and redirect
        # to the dashboard edit.
        if request.method == 'POST':
            form = plugin.get_initialised_edit_form_or_404(
                data=request.POST,
                files=request.FILES
            )
            if form.is_valid():
                # Saving the plugin form data.
                form.save_plugin_data(request=request)

                # Getting the plugin data.
                obj.plugin_data = form.get_plugin_data(request=request)

                # Save the object.
                obj.save()

                messages.info(
                    request,
                    _('The dashboard widget "{0}" was edited '
                      'successfully.').format(plugin.name)
                )

                # Redirect to edit dashboard view
                if obj.workspace:
                    return redirect(
                        'dash.edit_dashboard', workspace=obj.workspace.slug
                    )
                else:
                    return redirect('dash.edit_dashboard')

        else:
            form = plugin.get_initialised_edit_form_or_404()

        context.update({'form': form, 'plugin': plugin})

    if layout.edit_dashboard_entry_ajax_template_name:
        template_name_ajax = layout.edit_dashboard_entry_ajax_template_name

    context.update(
        {'edit_dashboard_entry_ajax_template_name': template_name_ajax}
    )

    if request.is_ajax():
        template_name = template_name_ajax
    elif layout.edit_dashboard_entry_template_name:
        template_name = layout.edit_dashboard_entry_template_name

    return render(request, template_name, context)


@login_required
@permission_required('dash.delete_dashboardentry')
def delete_dashboard_entry(request, entry_id):
    """Remove dashboard entry.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the dashboard entry to delete.
    :return django.http.HttpResponse:
    """
    try:
        obj = DashboardEntry._default_manager.select_related(
            'workspace'
        ).get(
            pk=entry_id,
            user=request.user
        )
        plugin = obj.get_plugin()
        plugin.request = request
        plugin._delete_plugin_data()
        workspace = getattr(obj.workspace, 'slug', None)
        obj.delete()

        if not request.is_ajax():
            messages.info(request, _('The dashboard widget "{0}" was deleted '
                                     'successfully.').format(plugin.name))

        if request.is_ajax():
            return HttpResponse(json.dumps({'success': 1}))
        else:
            # Redirect to dashboard view.
            if workspace:
                return redirect('dash.edit_dashboard', workspace=workspace)
            else:
                return redirect('dash.edit_dashboard')
    except ObjectDoesNotExist as err:
        if request.is_ajax():
            return HttpResponse(json.dumps({'success': 1}))
        raise Http404(err)

# ***************************************************************************
# ***************************************************************************
# ************************** Dashboard plugins  *****************************
# ***************************************************************************
# ***************************************************************************


@login_required
@permission_required('dash.add_dashboardentry')
def plugin_widgets(request,
                   placeholder_uid,
                   workspace=None,
                   position=None,
                   template_name='dash/plugin_widgets.html',
                   template_name_ajax='dash/plugin_widgets_ajax.html'):
    """Plugin widgets view.

    Lists all the widgets for the placeholder and workspace given.

    :param django.http.HttpRequest request:
    :param string placeholder_uid: Placeholder UID.
    :param mixed workspace:
    :param int position: Position on the dashboard to which the widget is to
        be added.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(
        layout_uid=dashboard_settings.layout_uid,
        as_instance=True
    )

    placeholder = layout.get_placeholder(placeholder_uid)

    if not validate_placeholder_uid(layout, placeholder_uid):
        raise Http404(
            gettext("Invalid placeholder: {0}").format(placeholder_uid)
        )

    occupied_cells = build_cells_matrix(
        request.user,
        layout,
        placeholder,
        workspace=workspace
    )

    # Here we checking if clipboard contains a plugin which is suitable for
    # being pasted into the cell given.
    paste_from_clipboard_url = None

    # First get the clipboard data.
    clipboard_plugin_data = get_plugin_data_from_clipboard(request, layout.uid)

    # If clipboard data is not empty, check if the data is suitable for
    # being pasted into the position given.
    if clipboard_plugin_data:
        can_paste_from_clipboard = can_paste_entry_from_clipboard(
            request=request,
            layout=layout,
            placeholder_uid=placeholder_uid,
            position=position,
            workspace=workspace
        )

        if can_paste_from_clipboard:
            kwargs = {
                'placeholder_uid': placeholder_uid,
                'position': position,
            }
            if workspace:
                kwargs.update({'workspace': workspace})

            paste_from_clipboard_url = reverse(
                'dash.paste_dashboard_entry',
                kwargs=kwargs
            )

    context = {
        'layout': layout,
        'grouped_widgets': get_widgets(
            layout,
            placeholder,
            request.user,
            workspace=workspace,
            position=position,
            occupied_cells=occupied_cells
        ),
        'dashboard_settings': dashboard_settings,
        'paste_from_clipboard_url': paste_from_clipboard_url,
    }

    if request.is_ajax():
        template_name = layout.plugin_widgets_template_name_ajax

    return render(request, template_name, context)

# ***************************************************************************
# ***************************************************************************
# **************** Create/edit/delete dashboard workspaces ******************
# ***************************************************************************
# ***************************************************************************


@login_required
@permission_required('dash.add_dashboardworkspace')
def create_dashboard_workspace(
    request,
    template_name='dash/create_dashboard_workspace.html',
    template_name_ajax='dash/create_dashboard_workspace_ajax.html'
):
    """Create dashboard workspace.

    :param django.http.HttpRequest request:
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(
        layout_uid=dashboard_settings.layout_uid,
        as_instance=True
    )

    if request.method == 'POST':
        form = DashboardWorkspaceForm(
            data=request.POST,
            files=request.FILES,
            different_layouts=dashboard_settings.allow_different_layouts
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            if not dashboard_settings.allow_different_layouts:
                obj.layout_uid = layout.uid
            obj.save()
            messages.info(
                request,
                _('The dashboard workspace "{0}" was '
                  'created successfully.').format(obj.name)
            )
            return redirect('dash.edit_dashboard', workspace=obj.slug)

    else:
        form = DashboardWorkspaceForm(
            initial={
                'user': request.user,
                'layout_uid': layout.uid,
            },
            different_layouts=dashboard_settings.allow_different_layouts
        )

    if layout.create_dashboard_workspace_ajax_template_name:
        template_name_ajax = \
            layout.create_dashboard_workspace_ajax_template_name

    if request.is_ajax():
        template_name = template_name_ajax
    elif layout.create_dashboard_workspace_template_name:
        template_name = layout.create_dashboard_workspace_template_name

    context = {
        'layout': layout,
        'form': form,
        'dashboard_settings': dashboard_settings,
    }

    return render(request, template_name, context)


@login_required
@permission_required('dash.change_dashboardworkspace')
def edit_dashboard_workspace(
    request,
    workspace_id,
    template_name='dash/edit_dashboard_workspace.html',
    template_name_ajax='dash/edit_dashboard_workspace_ajax.html'
):
    """Edit dashboard workspace.

    :param django.http.HttpRequest request:
    :param int workspace_id: DashboardWorkspace ID.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    # Check if user trying to edit the dashboard workspace actually owns it.
    try:
        obj = DashboardWorkspace._default_manager.get(
            pk=workspace_id,
            user=request.user
        )
    except ObjectDoesNotExist as err:
        raise Http404(err)

    layout = get_layout(layout_uid=obj.layout_uid, as_instance=True)

    if request.method == 'POST':
        form = DashboardWorkspaceForm(
            data=request.POST,
            files=request.FILES,
            instance=obj,
            different_layouts=dashboard_settings.allow_different_layouts
        )
        if form.is_valid():
            form.save(commit=False)
            obj.user = request.user
            if not dashboard_settings.allow_different_layouts:
                obj.layout_uid = layout.uid
            obj.save()
            messages.info(
                request,
                _('The dashboard workspace "{0}" was '
                  'edited successfully.').format(obj.name)
            )
            return redirect('dash.edit_dashboard', workspace=obj.slug)

    else:
        form = DashboardWorkspaceForm(
            instance=obj,
            different_layouts=dashboard_settings.allow_different_layouts
        )

    if layout.edit_dashboard_workspace_ajax_template_name:
        template_name_ajax = layout.edit_dashboard_workspace_ajax_template_name

    if request.is_ajax():
        template_name = template_name_ajax
    elif layout.edit_dashboard_workspace_template_name:
        template_name = layout.edit_dashboard_workspace_template_name

    context = {
        'layout': layout,
        'form': form,
        'workspace_id': workspace_id,
        'dashboard_settings': dashboard_settings,
    }

    return render(request, template_name, context)


@login_required
@permission_required('dash.delete_dashboardworkspace')
def delete_dashboard_workspace(
    request,
    workspace_id,
    template_name='dash/delete_dashboard_workspace.html',
    template_name_ajax='dash/delete_dashboard_workspace_ajax.html'
):
    """Delete dashboard workspace.

    :param django.http.HttpRequest request:
    :param int workspace_id: DashboardWorkspace id.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    # Check if user trying to edit the dashboard workspace actually owns it
    # and then delete the workspace.
    if (
        request.method == 'POST'
        and 'delete' in request.POST is None
        and request.POST.get('next', None)
    ):
        return redirect(request.POST.get('next'))

    try:
        obj = DashboardWorkspace._default_manager.get(
            pk=workspace_id,
            user=request.user
        )

    except ObjectDoesNotExist as err:
        raise Http404(err)

    layout = get_layout(layout_uid=obj.layout_uid, as_instance=True)

    if request.method == 'POST':
        if 'delete' in request.POST:
            workspace_name = obj.name

            # Getting the (frozen) queryset.
            dashboard_entries = DashboardEntry._default_manager.filter(
                user=request.user,
                layout_uid=layout.uid,
                workspace__id=workspace_id
            ).select_related(
                'workspace',
                'user'
            ).order_by(
                'placeholder_uid',
                'position'
            )[:]

            # Cleaning the plugin data for the deleted entries.
            clean_plugin_data(dashboard_entries, request=request)

            # Delete the workspace.
            obj.delete()

            messages.info(
                request,
                _('The dashboard workspace "{0}" was deleted '
                  'successfully.').format(workspace_name)
            )
            return redirect('dash.edit_dashboard')

        if request.POST.get('next', None):
            return redirect(request.POST.get('next'))

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'workspace': obj,
        'dashboard_settings': dashboard_settings,
    }

    return render(request, template_name, context)


@login_required
def dashboard_workspaces(
    request,
    workspace=None,
    template_name='dash/dashboard_workspaces.html',
    template_name_ajax='dash/dashboard_workspaces_ajax.html'
):
    """Workspaces list.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)

    context = get_workspaces(
        request.user,
        dashboard_settings.layout_uid,
        workspace,
        different_layouts=dashboard_settings.allow_different_layouts
    )

    if (
        dashboard_settings.allow_different_layouts
        and context['current_workspace']
    ):
        layout_uid = context['current_workspace'].layout_uid
    else:
        layout_uid = dashboard_settings.layout_uid

    layout = get_layout(layout_uid=layout_uid, as_instance=True)

    context.update({
        'layout': layout,
        'dashboard_settings': dashboard_settings,
    })

    if request.is_ajax():
        template_name = template_name_ajax

    return render(request, template_name, context)

# ***************************************************************************
# ***************************************************************************
# ************************* Dashboard settings ******************************
# ***************************************************************************
# ***************************************************************************


@login_required
@permission_required('dash.change_dashboardsettings')
def edit_dashboard_settings(
    request,
    template_name='dash/edit_dashboard_settings.html',
    template_name_ajax='dash/edit_dashboard_settings_ajax.html'
):
    """Edit dashboard settings.

    :param django.http.HttpRequest request:
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(
        layout_uid=dashboard_settings.layout_uid, as_instance=True
    )

    if request.method == 'POST':
        form = DashboardSettingsForm(
            data=request.POST,
            files=request.FILES,
            instance=dashboard_settings
        )
        if form.is_valid():
            form.save(commit=False)
            dashboard_settings.user = request.user
            dashboard_settings.save()
            messages.info(request, _('Dashboard settings were edited '
                                     'successfully.'))
            return redirect('dash.edit_dashboard')

    else:
        form = DashboardSettingsForm(instance=dashboard_settings)

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'form': form,
        'dashboard_settings': dashboard_settings,
    }

    return render(request, template_name, context)


@login_required
@permissions_required(satisfy=SATISFY_ALL,
                      perms=['dash.add_dashboardentry',
                             'dash.add_dashboardworkspace'])
def clone_dashboard_workspace(request, workspace_id):
    """Clones dashboard workspace."""
    redirect_to = request.GET.get('next', None)

    try:
        workspace = DashboardWorkspace._default_manager.get(pk=workspace_id)
    except DashboardWorkspace.DoesNotExist:
        messages.info(request, _("Invalid dashboard workspace."))
        if redirect_to:
            return redirect(redirect_to)
        else:
            return redirect('dash.edit_dashboard')

    if not (workspace.is_cloneable or request.user.pk == workspace.user.pk):
        messages.info(request, _("You are not allowed to clone the given "
                                 "workspace."))
        if redirect_to:
            return redirect(redirect_to)
        else:
            return redirect('dash.edit_dashboard')

    cloned_workspace = clone_workspace(workspace, request.user)

    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    cloned_workspace_layout = get_layout(
        layout_uid=workspace.layout_uid, as_instance=True
    )
    layout = get_layout(
        layout_uid=dashboard_settings.layout_uid, as_instance=True
    )

    if (
        workspace.layout_uid == layout.uid
        or dashboard_settings.allow_different_layouts
    ):
        messages.info(
            request,
            _("Dashboard workspace `{0}` was successfully cloned into "
              "`{1}`.".format(workspace.name, cloned_workspace.name))
        )
        return redirect('dash.edit_dashboard', workspace=cloned_workspace.slug)

    else:
        messages.info(
            request,
            _("Dashboard workspace `{0}` was successfully cloned into `{1}` "
              "(layout `{2}`), however your active layout is `{3}`. You "
              "should switch to layout `{4}` (in your dashboard settings) "
              "in order to see the cloned workspace."
              "".format(workspace.name,
                        cloned_workspace.name,
                        cloned_workspace_layout.name,
                        layout.name,
                        cloned_workspace_layout.name))
        )
        return redirect('dash.edit_dashboard')

# ***************************************************************************
# ***************************************************************************
# **************************** Clipboard views ******************************
# ***************************************************************************
# ***************************************************************************


@login_required
@use_clipboard_permission_required(
    raise_exception=RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT
)
def cut_dashboard_entry(request, entry_id):
    """Cut the given dashboard entry.

    It's not possible to remove undeletable entries.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the DashboardEntry to cut to clipboard.
    :return django.http.HttpResponse:
    """
    dashboard_entry = DashboardEntry._default_manager.select_related(
        'workspace'
    ).get(
        pk=entry_id,
        user=request.user
    )
    workspace = dashboard_entry.workspace
    plugin = dashboard_entry.get_plugin()

    cut_entry_to_clipboard(request, dashboard_entry)

    messages.info(request, _('The dashboard function "{0}" was successfully '
                             'cut and placed into the '
                             'clipboard.').format(safe_text(plugin.name)))

    if workspace and workspace.slug:
        return redirect('dash.edit_dashboard', workspace=workspace.slug)
    else:
        return redirect('dash.edit_dashboard')


@login_required
@use_clipboard_permission_required(
    raise_exception=RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT
)
def copy_dashboard_entry(request, entry_id):
    """Cut the given dashboard entry.

    It's not possible to remove undeletable entries.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the DashboardEntry to cut to clipboard.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    # dashboard_settings = get_or_create_dashboard_settings(request.user)
    # layout = get_layout(
    #     layout_uid=dashboard_settings.layout_uid, as_instance=True
    # )

    dashboard_entry = DashboardEntry._default_manager.select_related(
        'workspace'
    ).get(
        pk=entry_id,
        user=request.user
    )
    workspace = dashboard_entry.workspace
    plugin = dashboard_entry.get_plugin()

    copy_entry_to_clipboard(request, dashboard_entry)

    messages.info(request, _('The dashboard entry "{0}" was successfully '
                             'copied and placed into the '
                             'clipboard.').format(safe_text(plugin.name)))

    if workspace and workspace.slug:
        return redirect('dash.edit_dashboard', workspace=workspace.slug)
    else:
        return redirect('dash.edit_dashboard')


@login_required
@use_clipboard_permission_required(
    raise_exception=RAISE_EXCEPTION_WHEN_PERMISSIONS_INSUFFICIENT
)
def paste_dashboard_entry(request, placeholder_uid, position, workspace=None):
    """Paste the dashboard entry from clipboard if any available.

    :param django.http.HttpRequest request:
    :param str placeholder_uid:
    :param int position:
    :param str workspace: Workspace slug.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(
        layout_uid=dashboard_settings.layout_uid,
        as_instance=True
    )

    try:
        plugin_uid, success = paste_entry_from_clipboard(
            request,
            layout,
            placeholder_uid,
            position,
            workspace=workspace
        )
    except Exception as err:
        plugin_uid, success = str(err), False

    if plugin_uid and success:
        plugin = plugin_registry.get(plugin_uid)
        messages.info(
            request,
            _('The dashboard entry "{0}" was successfully pasted from '
              'clipboard.').format(safe_text(plugin.name))
        )
    else:
        # In case if not success, ``plugin_uid`` would be holding the error
        # message.
        messages.info(
            request,
            _('Problems occurred while pasting from '
              'clipboard. {0}'.format(safe_text(plugin_uid)))
        )

    if workspace:
        return redirect('dash.edit_dashboard', workspace=workspace)
    else:
        return redirect('dash.edit_dashboard')
