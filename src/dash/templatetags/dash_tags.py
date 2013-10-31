__all__ = ('get_dash_plugin',)

from django.template import Library, TemplateSyntaxError, Node
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from dash.settings import ACTIVE_LAYOUT, DISPLAY_AUTH_LINK
from dash.utils import get_workspaces

register = Library()

# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************
# **************************** General Dash tags ****************************************
# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************

class GetDashPluginNode(Node):
    """
    Node for ``get_dash_plugin`` tag.
    """
    def __init__(self, dashboard_entry, as_var=None):
        self.dashboard_entry = dashboard_entry
        self.as_var = as_var

    def render(self, context):
        request = context['request']
        dashboard_entry = self.dashboard_entry.resolve(context, True)

        plugin = dashboard_entry.get_plugin(request=request)
        context[self.as_var] = plugin
        return ''


@register.tag
def get_dash_plugin(parser, token):
    """
    Gets the plugin. Note, that ``dashboard_entry`` shall be a instance of ``dash.models.DashboardEntry``.
    
    :syntax:

        {% get_dash_plugin dashboard_entry as [context_var_name] %}

    :example:

        {% get_dash_plugin dashboard_entry as plugin %}

        {% get_dash_plugin dashboard_entry as plugin %}
        {{ plugin.render }}
    """
    bits = token.contents.split()

    if 4 == len(bits):
        if 'as' != bits[-2]:
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of arguments.".format(bits[0])
                )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid syntax.".format(bits[0])
            )

    dashboard_entry = parser.compile_filter(bits[1])

    return GetDashPluginNode(dashboard_entry=dashboard_entry, as_var=as_var)


class GetDashWorkspacesNode(Node):
    """
    Node for ``get_dash_workspaces`` tag.
    """
    def __init__(self, layout_uid=None, edit_mode=False):
        self.layout_uid = layout_uid
        self.edit_mode = edit_mode

    def render(self, context):
        try:
            request = context['request']
            user = request.user
        except Exception as e:
            return ''
        
        if self.layout_uid:
            layout_uid = self.layout_uid.resolve(context, True)

        else:
            try:
                layout_uid = context['layout'].uid
            except Exception as e:
                layout_uid = ACTIVE_LAYOUT

        workspaces = get_workspaces(user=user, layout_uid=layout_uid)

        context['workspaces'] = workspaces['workspaces']
        context['next_workspace'] = workspaces['next_workspace']
        context['previous_workspace'] = workspaces['previous_workspace']
        context['current_workspace'] = workspaces['current_workspace']
        return ''


@register.tag
def get_dash_workspaces(parser, token):
    """
    Gets the workspaces queryset

    :syntax:

        {% get_dash_workspaces [layout_uid] mode [edit_mode] %}

    :example:

        {% get_dash_workspaces layout.uid %}

        {% get_dash_workspaces layout.uid 1 %}
    """
    bits = token.contents.split()

    if len(bits) not in (1, 2, 3, 4):
        raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of arguments.".format(bits[0])
                )

    if 4 == len(bits):
        layout_uid = parser.compile_filter(bits[1])
        edit_mode = bits[-1]

    elif 3 == len(bits):
        layout_uid = None
        edit_mode = bits[-1]

    elif 2 == len(bits):
        layout_uid = parser.compile_filter(bits[1])
        edit_mode = False

    return GetDashWorkspacesNode(layout_uid=layout_uid, edit_mode=edit_mode)


# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************
# **************************** Additional Dash tags *************************************
# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************

def render_auth_link(context):
    """
    Render logout link.
    """
    if not DISPLAY_AUTH_LINK:
        return {}

    request = context.get('request', None)
    if request and request.user.is_authenticated():
        try:
            auth_url = settings.LOGOUT_URL
            auth_icon_class = 'icon-signout'
            auth_link_text = _('Log out')
        except Exception as e:
            auth_url = ''
            auth_icon_class = ''
            auth_link_text = ''
    else:
        try:
            auth_url = settings.LOGIN_URL
            auth_icon_class = 'icon-signin'
            auth_link_text = _('Log in')
        except Exception as e:
            auth_url = ''
            auth_icon_class = ''
            auth_link_text = ''

    return {
        'auth_link': auth_url,
        'auth_icon_class': auth_icon_class,
        'auth_link_text': auth_link_text
    }

# For backwards compatibilty. TODO: Raise deprecation warning.
def render_logout_link(context):
    return render_auth_link(context)

register.inclusion_tag('dash/snippets/render_auth_link.html', takes_context=True)(render_auth_link)
register.inclusion_tag('dash/snippets/render_auth_link.html', takes_context=True)(render_logout_link)

# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************
# **************************** Permission tags ******************************************
# ***************************************************************************************
# ***************************************************************************************
# ***************************************************************************************

class HasEditDashboardPermissionsNode(Node):
    """
    Node for ``has_edit_dashboard_permissions`` tag.
    """
    def __init__(self, as_var=None):
        self.as_var = as_var

    def render(self, context):
        try:
            perms = context['perms']
        except Exception as e:
            if self.as_var:
                context[self.as_var] = False
                return ''
            else:
                return False

        perms_required = [
            'dash.add_dashboardentry', 'dash.change_dashboardentry', 'dash.delete_dashboardentry',
            'dash.add_dashboardworkspace', 'dash.change_dashboardworkspace', 'dash.delete_dashboardworkspace',
            'dash.add_dashboardsettings', 'dash.change_dashboardsettings', 'dash.delete_dashboardsettings',
        ]

        for perm in perms_required:
            if perm in perms:
                if self.as_var:
                    context[self.as_var] = True
                    return ''
                else:
                    return True

        if self.as_var:
            context[self.as_var] = False
            return ''
        else:
            return False


@register.tag
def has_edit_dashboard_permissions(parser, token):
    """
    Gets the workspaces queryset

    :syntax:

        {% has_edit_dashboard_permissions as [var_name] %}

    :example:

        {% has_edit_dashboard_permissions %}

        or

        {% has_edit_dashboard_permissions as has_permissions %}
    """
    bits = token.contents.split()

    if len(bits) not in (1, 3):
        raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of arguments.".format(bits[0])
                )

    if 3 == len(bits):
        as_var = bits[-1]

    else:
        as_var = None

    return HasEditDashboardPermissionsNode(as_var=as_var)
