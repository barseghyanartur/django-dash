from django import forms
from django.conf import settings
from django.template.base import TemplateSyntaxError, Node
from django.template.library import Library
from django.utils.translation import gettext_lazy as _

from ..settings import ACTIVE_LAYOUT, DISPLAY_AUTH_LINK
from ..utils import get_workspaces

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'get_dash_plugin',
    'get_dash_workspaces',
    'has_edit_dashboard_permissions',
    'render_auth_link',
)


register = Library()

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** General Dash tags ******************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


class GetDashPluginNode(Node):
    """Node for ``get_dash_plugin`` tag."""

    def __init__(self, dashboard_entry, as_var=None):
        self.dashboard_entry = dashboard_entry
        self.as_var = as_var

    def render(self, context):
        """Render."""
        request = context['request']
        dashboard_entry = self.dashboard_entry.resolve(context, True)

        plugin = dashboard_entry.get_plugin(request=request)
        context[self.as_var] = plugin
        return ''


@register.tag
def get_dash_plugin(parser, token):
    """Get the plugin.

    Note, that ``dashboard_entry`` shall be a instance of
    ``dash.models.DashboardEntry``.

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
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(bits[0])
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid syntax."
            "".format(bits[0])
        )

    dashboard_entry = parser.compile_filter(bits[1])

    return GetDashPluginNode(dashboard_entry=dashboard_entry, as_var=as_var)


class GetDashWorkspacesNode(Node):
    """Node for ``get_dash_workspaces`` tag."""

    def __init__(self, layout_uid=None, edit_mode=False):
        self.layout_uid = layout_uid
        self.edit_mode = edit_mode

    def render(self, context):
        """Render."""
        try:
            request = context['request']
            user = request.user
        except Exception:
            return ''

        if self.layout_uid:
            layout_uid = self.layout_uid.resolve(context, True)

        else:
            try:
                layout_uid = context['layout'].uid
            except Exception:
                layout_uid = ACTIVE_LAYOUT

        workspaces = get_workspaces(user=user, layout_uid=layout_uid)

        context['workspaces'] = workspaces['workspaces']
        context['next_workspace'] = workspaces['next_workspace']
        context['previous_workspace'] = workspaces['previous_workspace']
        context['current_workspace'] = workspaces['current_workspace']
        return ''


@register.tag
def get_dash_workspaces(parser, token):
    """Get the workspaces queryset

    :syntax:

        {% get_dash_workspaces [layout_uid] mode [edit_mode] %}

    :example:

        {% get_dash_workspaces layout.uid %}

        {% get_dash_workspaces layout.uid 1 %}
    """
    bits = token.contents.split()

    if len(bits) not in (1, 2, 3, 4):
        raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number "
                "of arguments.".format(bits[0])
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


# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** Additional Dash tags ***************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

def render_auth_link(context):
    """Render logout link."""
    if not DISPLAY_AUTH_LINK:
        return {}

    request = context.get('request', None)
    user_is_authenticated = request.user.is_authenticated

    if request and user_is_authenticated:
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


# For backwards compatibility. TODO: Raise deprecation warning.
def render_logout_link(context):
    """Render logout link.

    Old deprecated thing.
    """
    return render_auth_link(context)


register.inclusion_tag('dash/snippets/render_auth_link.html',
                       takes_context=True)(render_auth_link)
register.inclusion_tag('dash/snippets/render_auth_link.html',
                       takes_context=True)(render_logout_link)

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** Permission tags ********************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


class HasEditDashboardPermissionsNode(Node):
    """Node for ``has_edit_dashboard_permissions`` tag."""

    def __init__(self, as_var=None):
        self.as_var = as_var

    def render(self, context):
        """Render."""
        try:
            perms = context['perms']
        except Exception as e:
            if self.as_var:
                context[self.as_var] = False
                return ''
            else:
                return False

        perms_required = [
            'dash.add_dashboardentry',
            'dash.change_dashboardentry',
            'dash.delete_dashboardentry',
            'dash.add_dashboardworkspace',
            'dash.change_dashboardworkspace',
            'dash.delete_dashboardworkspace',
            'dash.add_dashboardsettings',
            'dash.change_dashboardsettings',
            'dash.delete_dashboardsettings',
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
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(bits[0])
                )

    if 3 == len(bits):
        as_var = bits[-1]

    else:
        as_var = None

    return HasEditDashboardPermissionsNode(as_var=as_var)

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************
# **************************** General Django tags ****************************
# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


class FormFieldType(object):
    """Form field type container."""

    is_checkbox = False
    is_password = False
    is_hidden = False
    is_text = False
    is_radio = False
    is_textarea = False

    def __init__(self, properties=[]):
        """
        By default all of them are false. Provide only property
        names that should be set to True.
        """
        for prop in properties:
            setattr(self, prop, True)


class GetFormFieldTypeNode(Node):
    """Node for ``get_form_field_type`` tag."""

    def __init__(self, field, as_var=None):
        self.field = field
        self.as_var = as_var

    def render(self, context):
        """Render."""
        field = self.field.resolve(context, True)
        properties = []

        if isinstance(field.field.widget, forms.CheckboxInput):
            properties.append('is_checkbox')

        if isinstance(field.field.widget, forms.CheckboxSelectMultiple):
            properties.append('is_checkbox_multiple')

        if isinstance(field.field.widget, forms.RadioSelect):
            properties.append('is_radio')

        res = FormFieldType(properties)

        context[self.as_var] = res
        return ''


@register.tag
def get_form_field_type(parser, token):
    """Get form field type.

    Syntax::

        {% get_form_field_type [field] as [context_var_name] %}
    Example::

        {% get_form_field_type form.field as form_field_type %}
        {% if form_field_type.is_checkbox %}
        ...
        {% endif %}
    """
    bits = token.contents.split()

    if 4 == len(bits):
        if 'as' != bits[-2]:
            raise TemplateSyntaxError(
                "Invalid syntax for {0}. Incorrect number of "
                "arguments.".format(
                    bits[0]
                )
            )
        as_var = bits[-1]
    else:
        raise TemplateSyntaxError(
            "Invalid syntax for {0}. See docs for valid "
            "syntax.".format(bits[0])
        )

    field = parser.compile_filter(bits[1])

    return GetFormFieldTypeNode(field=field, as_var=as_var)
