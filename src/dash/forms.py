__title__ = 'dash.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DashboardWorkspaceForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import get_registered_layouts
from dash.models import DashboardWorkspace, DashboardSettings, DashboardPlugin
from dash.constants import ACTION_CHOICES

class DashboardWorkspaceForm(forms.ModelForm):
    """
    Dashboard workspace form.
    """
    layout_uid = forms.TypedChoiceField(
        label=_('Layout'),
        choices=get_registered_layouts(),
        empty_value=None,
    )

    class Meta:
        model = DashboardWorkspace
        fields = ('layout_uid', 'user', 'name', 'is_public', 'is_clonable')

    def __init__(self, *args, **kwargs):
        different_layouts = kwargs.pop('different_layouts', False)
        super(DashboardWorkspaceForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.widgets.HiddenInput()
        if not different_layouts:
            self.fields['layout_uid'].widget = forms.widgets.HiddenInput()


class DashboardSettingsForm(forms.ModelForm):
    """
    Dashboard settings form.
    """
    class Meta:
        model = DashboardSettings
        fields = ('user', 'layout_uid', 'title', 'is_public')

    def __init__(self, *args, **kwargs):
        super(DashboardSettingsForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.widgets.HiddenInput()


class BulkChangeDashboardPluginsForm(forms.ModelForm):
    """
    Bulk change dashboard plugins form.

    - `selected_dashboard_plugins` (str): List of comma separated values to be changed.
    - `users_action` (int): For indicating wheither the users shall be appended to the dashbard plugins or replaced.
    - `groups_action` (int): For indicating wheither the groups shall be appended to the dashboard plugins or replaced.
    """
    selected_dashboard_plugins = forms.CharField(
        required=True, label=_("Selected dashboard plugins"), widget=forms.widgets.HiddenInput
        )
    users_action = forms.ChoiceField(
        required = False,
        label = _("Users action"),
        choices = ACTION_CHOICES,
        help_text = _("If set to ``replace``, the groups are replaced; otherwise - appended.")
        )
    groups_action = forms.ChoiceField(
        required = False,
        label = _("Groups action"),
        choices = ACTION_CHOICES,
        help_text = _("If set to ``replace``, the groups are replaced; otherwise - appended.")
        )

    class Meta:
        model = DashboardPlugin
        fields = ['groups', 'groups_action', 'users', 'users_action',]

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

    def __init__(self, *args, **kwargs):
        super(BulkChangeDashboardPluginsForm, self).__init__(*args, **kwargs)
        self.fields['users'].required = False
        self.fields['groups'].required = False
