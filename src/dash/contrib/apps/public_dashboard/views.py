import logging

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from ....base import get_layout
from ....helpers import iterable_to_dict
from ....models import DashboardEntry
from ....utils import get_user_plugins, get_workspaces, get_dashboard_settings
from ....settings import AUTH_LOGIN_URL_NAME, AUTH_LOGOUT_URL_NAME


__title__ = 'dash.contrib.apps.public_dashboard.views'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('public_dashboard',)

logger = logging.getLogger(__name__)


def public_dashboard(request,
                     username,
                     workspace=None,
                     template_name='public_dashboard/public_dashboard.html'):
    """Public dashboard.

    :param django.http.HttpRequest request:
    :param string username:
    :param string workspace: Workspace slug.
    :param string template_name:
    :return django.http.HttpResponse:
    """
    # Getting dashboard settings for the user. Then get users' layout.
    dashboard_settings = get_dashboard_settings(username)
    if dashboard_settings:
        layout = get_layout(layout_uid=dashboard_settings.layout_uid,
                            as_instance=True)
        user = dashboard_settings.user
    else:
        raise Http404

    # Getting the list of plugins that user is allowed to use.
    registered_plugins = get_user_plugins(user)
    user_plugin_uids = [uid for uid, repr in registered_plugins]

    logger.debug(user_plugin_uids)

    # A complex query required. All entries shall be taken from default
    # dashboard (no workspace) and joined with all entries of workspaces
    # set to be public. Getting the (frozen) queryset.
    if workspace:
        entries_q = Q(
            user=user,
            layout_uid=layout.uid,
            workspace__slug=workspace,
            workspace__is_public=True,
            plugin_uid__in=user_plugin_uids
        )
    else:
        entries_q = Q(user=user, layout_uid=layout.uid, workspace=None)

    dashboard_entries = DashboardEntry._default_manager \
        .filter(entries_q) \
        .select_related('workspace', 'user') \
        .order_by('placeholder_uid', 'position')[:]

    # logger.debug(dashboard_entries)

    placeholders = layout.get_placeholder_instances(dashboard_entries,
                                                    request=request)

    layout.collect_widget_media(dashboard_entries)

    context = {
        'placeholders': placeholders,
        'placeholders_dict': iterable_to_dict(
            placeholders,
            key_attr_name='uid'
        ),
        'css': layout.get_css(placeholders),
        'layout': layout,
        'user': user,
        'master_template': layout.get_view_template_name(
            request,
            origin='dash.public_dashboard'
        ),
        'dashboard_settings': dashboard_settings,
        'AUTH_LOGIN_URL_NAME': AUTH_LOGIN_URL_NAME,
        'AUTH_LOGOUT_URL_NAME': AUTH_LOGOUT_URL_NAME,
    }

    workspaces = get_workspaces(user, layout.uid, workspace, public=True)

    # If workspace with slug given is not found in the list of workspaces
    # redirect to the default dashboard.
    if workspaces['current_workspace_not_found']:
        messages.info(
            request,
            _('The workspace with slug "{0}" does not exist.'
              '').format(workspace)
        )
        return redirect('dash.public_dashboard', username=username)

    context.update(workspaces)

    return render(request, template_name, context)
