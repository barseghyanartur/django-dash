__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

import json

from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from dash.base import validate_plugin_uid
from dash.base import get_layout, plugin_registry, validate_placeholder_uid
from dash.models import DashboardEntry, DashboardWorkspace
from dash.decorators import edit_dashboard_permission_required
from dash.helpers import slugify_workspace, iterable_to_dict
from dash.utils import get_widgets, get_user_plugins, get_workspaces, build_cells_matrix
from dash.utils import get_or_create_dashboard_settings, get_public_dashboard_url, clean_plugin_data
from dash.forms import DashboardWorkspaceForm, DashboardSettingsForm

@login_required
def dashboard(request, workspace=None):
    """
    Dashboard.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug. If given, the workspace loaded. Otherwise we deal with no workspace.
    :return django.http.HttpResponse:
    """
    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(request.user)
    user_plugin_uids = [uid for uid, repr in registered_plugins]

    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    # Getting the (frozen) queryset.
    dashboard_entries = DashboardEntry._default_manager \
                                      .get_for_user(user=request.user, layout_uid=layout.uid, workspace=workspace) \
                                      .select_related('workspace', 'user') \
                                      .filter(plugin_uid__in=user_plugin_uids) \
                                      .order_by('placeholder_uid', 'position')[:]

    placeholders = layout.get_placeholder_instances(dashboard_entries, request=request)

    layout.collect_widget_media(dashboard_entries)

    context = {
        'placeholders': placeholders,
        'placeholders_dict': iterable_to_dict(placeholders, key_attr_name='uid'),
        'css': layout.get_css(placeholders),
        'layout': layout,
        'dashboard_settings': dashboard_settings
    }

    workspaces = get_workspaces(request.user, layout.uid, workspace)

    # If workspace with slug given is not found in the list of workspaces
    # redirect to the default dashboard.
    if workspaces['current_workspace_not_found']:
        messages.info(
            request,
            _('The workspace with slug "{0}" does not belong to layout "{1}".').format(workspace, layout.name)
            )
        return redirect('dash.edit_dashboard')

    context.update(workspaces)

    context.update({'public_dashboard_url': get_public_dashboard_url(dashboard_settings)})

    template_name = layout.get_view_template_name(request)

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@edit_dashboard_permission_required()
def edit_dashboard(request, workspace=None):
    """
    Edit dashboard.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug. If given, the workspace loaded. Otherwise we deal with no workspace.
    :return django.http.HttpResponse:
    """
    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(request.user)
    user_plugin_uids = [uid for uid, repr in registered_plugins]

    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    # Getting the (frozen) queryset.
    dashboard_entries = DashboardEntry._default_manager \
                                      .get_for_user(user=request.user, layout_uid=layout.uid, workspace=workspace) \
                                      .select_related('workspace', 'user') \
                                      .filter(plugin_uid__in=user_plugin_uids) \
                                      .order_by('placeholder_uid', 'position')[:]

    placeholders = layout.get_placeholder_instances(dashboard_entries, workspace=workspace, request=request)

    layout.collect_widget_media(dashboard_entries)

    context = {
        'placeholders': placeholders,
        'placeholders_dict': iterable_to_dict(placeholders, key_attr_name='uid'),
        'css': layout.get_css(placeholders),
        'layout': layout,
        'edit_mode': True,
        'dashboard_settings': dashboard_settings
    }

    workspaces = get_workspaces(request.user, layout.uid, workspace)

    # If workspace with slug given is not found in the list of workspaces
    # redirect to the default dashboard.
    if workspaces['current_workspace_not_found']:
        messages.info(
            request,
            _('The workspace with slug "{0}" does not belong to layout "{1}".').format(workspace, layout.name)
            )
        return redirect('dash.edit_dashboard')

    context.update(workspaces)

    context.update({'public_dashboard_url': get_public_dashboard_url(dashboard_settings)})

    template_name = layout.get_edit_template_name(request)

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.add_dashboardentry')
def add_dashboard_entry(request, placeholder_uid, plugin_uid, workspace=None, position=None, \
                        template_name='dash/add_dashboard_entry.html', \
                        template_name_ajax='dash/add_dashboard_entry_ajax.html'):
    """
    Add dashboard entry.

    :param django.http.HttpRequest request:
    :param string placeholder_uid: Placeholder UID.
    :param string plugin_uid: Plugin UID.
    :param string workspace: Workspace slug.
    :param int position: If given, provided as position for the plugin (conflict resolution should take place).
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    if not validate_placeholder_uid(layout, placeholder_uid):
        raise Http404(_("Invalid placeholder: {0}").format(placeholder))

    if not validate_plugin_uid(plugin_uid):
        raise Http404(_("Invalid plugin name: {0}").format(plugin_uid))

    plugin = plugin_registry.get(plugin_uid)(layout.uid, placeholder_uid)
    plugin.request = request

    if plugin.add_form_template:
        template_name = plugin.add_form_template

    # Template context
    context = {
        'layout': layout,
        'dashboard_settings': dashboard_settings
    }

    obj = DashboardEntry()
    obj.layout_uid = layout.uid
    obj.placeholder_uid = placeholder_uid
    obj.plugin_uid = plugin_uid
    obj.user = request.user

    # If plugin has form, it is configurable which means we have to load the plugin form and validate user input.
    plugin_form = plugin.get_form()
    if plugin_form:
        # If POST request and form data is valid, save the data and redirect to the dashboard edit.
        if 'POST' == request.method:
            form = plugin.get_initialised_create_form_or_404(data=request.POST, files=request.FILES)
            if form.is_valid():
                # Saving the plugin form data.
                form.save_plugin_data(request=request)

                # Getting the plugin data.
                obj.plugin_data = form.get_plugin_data(request=request)

                # Handling the workspace.
                obj.workspace = None
                if workspace:
                    workspace_slug = slugify_workspace(workspace)
                    try:
                        obj.workspace = DashboardWorkspace._default_manager.get(
                            slug=workspace_slug, user=request.user, layout_uid = layout.uid
                            )
                    except ObjectDoesNotExist as e:
                        messages.info(
                            request,
                            _('The workspace with slug "{0}" does not belong to '
                              'layout "{1}".').format(workspace_slug, layout.name)
                            )
                        return redirect('dash.edit_dashboard')

                # If position given, use it.
                try:
                    position = int(position)
                except Exception as e:
                    position = None

                if position:
                    obj.position = position

                # Save the object.
                obj.save()

                messages.info(
                    request,
                    _('The dashboard widget "{0}" was added successfully.').format(plugin.name)
                    )

                # Redirect to the dashboard view.
                if obj.workspace:
                    return redirect('dash.edit_dashboard', workspace=obj.workspace.slug)
                else:
                    return redirect('dash.edit_dashboard')

        # If POST but data invalid, show the form with errors.
        else:
            form = plugin.get_initialised_create_form_or_404()

        context.update({'form': form, 'plugin_uid': plugin_uid, 'plugin': plugin})

    # If plugin is not configurable, it's just saved as is.
    else:
        obj.save()
        return redirect('dash.edit_dashboard')

    if request.is_ajax():
        template_name = template_name_ajax

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.change_dashboardentry')
def edit_dashboard_entry(request, entry_id, template_name='dash/edit_dashboard_entry.html', \
                         template_name_ajax='dash/edit_dashboard_entry_ajax.html'):
    """
    Edit dashboard entry.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the dashboard entry to edit.
    :param string template_name:
    :param string template_name_ajax: Tempalte used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    try:
        obj = DashboardEntry._default_manager.select_related('workspace').get(pk=entry_id, user=request.user)
    except ObjectDoesNotExist as e:
        raise Http404(e)

    plugin = obj.get_plugin(fetch_related_data=True)
    plugin.request = request

    if plugin.edit_form_template:
        template_name = plugin.edit_form_template

    # Template context
    context = {
        'layout': layout,
        'dashboard_settings': dashboard_settings
    }

    # If plugin has form, it is configurable which means we have to load the plugin form and validate user input.
    plugin_form = plugin.get_form()
    if plugin_form:
        # If POST request and form data is valid, save the data and redirect to the dashboard edit.
        if 'POST' == request.method:
            form = plugin.get_initialised_edit_form_or_404(data=request.POST, files=request.FILES)
            if form.is_valid():
                # Saving the plugin form data.
                form.save_plugin_data(request=request)

                # Getting the plugin data.
                obj.plugin_data = form.get_plugin_data(request=request)

                # Save the object.
                obj.save()

                messages.info(
                    request,
                    _('The dashboard widget "{0}" was edited successfully.').format(plugin.name)
                    )

                # Redirect to edit dashboard view
                if obj.workspace:
                    return redirect('dash.edit_dashboard', workspace=obj.workspace.slug)
                else:
                    return redirect('dash.edit_dashboard')

        else:
            form = plugin.get_initialised_edit_form_or_404()

        context.update({'form': form, 'plugin': plugin})

    if request.is_ajax():
        template_name = template_name_ajax

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.delete_dashboardentry')
def delete_dashboard_entry(request, entry_id):
    """
    Remove dashboard entry.

    :param django.http.HttpRequest request:
    :param int entry_id: ID of the dashboard entry to delete.
    :return django.http.HttpResponse:
    """
    try:
        obj = DashboardEntry._default_manager.select_related('workspace').get(pk=entry_id, user=request.user)
        plugin = obj.get_plugin()
        plugin.request = request
        plugin.delete_plugin_data()
        workspace = getattr(obj.workspace, 'slug', None)
        obj.delete()

        if not request.is_ajax():
            messages.info(request, _('The dashboard widget "{0}" was deleted successfully.').format(plugin.name))

        if request.is_ajax():
            return HttpResponse(json.dumps({'success': 1}))
        else:
            # Redirect to dashboard view.
            if workspace:
                return redirect('dash.edit_dashboard', workspace=workspace)
            else:
                return redirect('dash.edit_dashboard')
    except ObjectDoesNotExist as e:
        if request.is_ajax():
            return HttpResponse(json.dumps({'success': 1}))
        raise Http404(e)

@login_required
@permission_required('dash.add_dashboardentry')
def plugin_widgets(request, placeholder_uid, workspace=None, position=None, \
                   template_name='dash/plugin_widgets.html', template_name_ajax='dash/plugin_widgets_ajax.html'):
    """
    Plugin widgets view. Lists all the widgets for the placeholder and workspace given.

    :param django.http.HttpRequest request:
    :param string placeholder_uid: Placeholder UID.
    :param int position: Position on the dashboard to which the widget is to be added.
    :param string template_name:
    :param string template_name_ajax: Tempalte used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    placeholder = layout.get_placeholder(placeholder_uid)

    if not validate_placeholder_uid(layout, placeholder_uid):
        raise Http404(_("Invalid placeholder: {0}").format(placeholder_uid))

    occupied_cells = build_cells_matrix(request.user, layout, placeholder, workspace=workspace)

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
        'dashboard_settings': dashboard_settings
    }

    if request.is_ajax():
        template_name = template_name_ajax
    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.add_dashboardworkspace')
def create_dashboard_workspace(request, template_name='dash/create_dashboard_workspace.html', \
                               template_name_ajax='dash/create_dashboard_workspace_ajax.html'):
    """
    Create dashboard workspace.

    :param django.http.HttpRequest request:
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)


    if 'POST' == request.method:
        form = DashboardWorkspaceForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.layout_uid = layout.uid
            obj.save()
            messages.info(request, _('The dashboard workspace "{0}" was created successfully.').format(obj.name))
            return redirect('dash.edit_dashboard', workspace=obj.slug)

    else:
        form = DashboardWorkspaceForm(initial={'user': request.user})

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'form': form,
        'dashboard_settings': dashboard_settings
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.change_dashboardworkspace')
def edit_dashboard_workspace(request, workspace_id, template_name='dash/edit_dashboard_workspace.html', \
                             template_name_ajax='dash/edit_dashboard_workspace_ajax.html'):
    """
    Edit dashboard workspace.

    :param django.http.HttpRequest request:
    :param int workspace_id: DashboardWorkspace ID.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    # Check if user trying to edit the dashboard workspace actually owns it.
    try:
        obj = DashboardWorkspace._default_manager.get(pk=workspace_id, user=request.user)
    except ObjectDoesNotExist as e:
        raise Http404(e)

    if 'POST' == request.method:
        form = DashboardWorkspaceForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            form.save(commit=False)
            obj.user = request.user
            obj.layout_uid = layout.uid
            obj.save()
            messages.info(request, _('The dashboard workspace "{0}" was edited successfully.').format(obj.name))
            return redirect('dash.edit_dashboard', workspace=obj.slug)

    else:
        form = DashboardWorkspaceForm(instance=obj)

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'form': form,
        'workspace_id': workspace_id,
        'dashboard_settings': dashboard_settings
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.delete_dashboardworkspace')
def delete_dashboard_workspace(request, workspace_id, template_name='dash/delete_dashboard_workspace.html', \
                               template_name_ajax='dash/delete_dashboard_workspace_ajax.html'):
    """
    Delete dashboard workspace.

    :param django.http.HttpRequest request:
    :param int workspace_id: DashboardWorkspace id.
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    # Check if user trying to edit the dashboard workspace actually owns it and then delete the workspace.
    if 'POST' == request.method and 'delete' in request.POST is None and request.POST.get('next', None):
        return redirect(request.POST.get('next'))

    try:
        obj = DashboardWorkspace._default_manager.get(pk=workspace_id, user=request.user)

    except ObjectDoesNotExist as e:
        raise Http404(e)

    if 'POST' == request.method:
        if 'delete' in request.POST:
            workspace_name = obj.name

            # Getting the (frozen) queryset.
            dashboard_entries = DashboardEntry._default_manager \
                                    .filter(user=request.user, layout_uid=layout.uid, workspace__id=workspace_id) \
                                    .select_related('workspace', 'user') \
                                    .order_by('placeholder_uid', 'position')[:]

            # Cleaning the plugin data for the deleted entries.
            clean_plugin_data(dashboard_entries, request=request)

            # Delete the workspace.
            obj.delete()

            messages.info(request, _('The dashboard workspace "{0}" was deleted successfully.').format(workspace_name))
            return redirect('dash.edit_dashboard')

        if request.POST.get('next', None):
            return redirect(request.POST.get('next'))

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'workspace': obj,
        'dashboard_settings': dashboard_settings
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
def dashboard_workspaces(request, workspace=None, template_name='dash/dashboard_workspaces.html', \
                         template_name_ajax='dash/dashboard_workspaces_ajax.html'):
    """
    Workspaces list.

    :param django.http.HttpRequest request:
    :param string workspace: Workspace slug.
    :param string template_name:
    :param string template_name_ajax: Tempalte used for AJAX requests.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    context = {
        'layout': layout,
        'dashboard_settings': dashboard_settings
    }
    context.update(get_workspaces(request.user, layout.uid, workspace))

    if request.is_ajax():
        template_name = template_name_ajax
    return render_to_response(template_name, context, context_instance=RequestContext(request))

@login_required
@permission_required('dash.change_dashboardsettings')
def edit_dashboard_settings(request, template_name='dash/edit_dashboard_settings.html', \
                            template_name_ajax='dash/edit_dashboard_settings_ajax.html'):
    """
    Edit dashboard settings.

    :param django.http.HttpRequest request:
    :param string template_name:
    :param string template_name_ajax: Template used for AJAX calls.
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_or_create_dashboard_settings(request.user)
    layout = get_layout(layout_uid=dashboard_settings.layout_uid, as_instance=True)

    if 'POST' == request.method:
        form = DashboardSettingsForm(data=request.POST, files=request.FILES, instance=dashboard_settings)
        if form.is_valid():
            form.save(commit=False)
            dashboard_settings.user = request.user
            dashboard_settings.save()
            messages.info(request, _('Dashboard settings were edited successfully.'))
            return redirect('dash.edit_dashboard')

    else:
        form = DashboardSettingsForm(instance=dashboard_settings)

    if request.is_ajax():
        template_name = template_name_ajax

    context = {
        'layout': layout,
        'form': form,
        'dashboard_settings': dashboard_settings
    }

    return render_to_response(template_name, context, context_instance=RequestContext(request))
