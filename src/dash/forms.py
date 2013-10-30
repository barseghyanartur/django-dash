__all__ = ('DashboardWorkspaceForm',)

from django import forms

from dash.models import DashboardWorkspace, DashboardSettings

class DashboardWorkspaceForm(forms.ModelForm):
    """
    Dashboard workspace form.
    """
    class Meta:
        model = DashboardWorkspace
        exclude = ('position', 'layout_uid')

    def __init__(self, *args, **kwargs):
        super(DashboardWorkspaceForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.widgets.HiddenInput()
        #self.fields['layout_uid'].widget = forms.widgets.HiddenInput()


class DashboardSettingsForm(forms.ModelForm):
    """
    Dashboard settings form.
    """
    class Meta:
        model = DashboardSettings

    def __init__(self, *args, **kwargs):
        super(DashboardSettingsForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.widgets.HiddenInput()
