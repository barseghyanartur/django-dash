__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('MemoForm', 'TinyMCEMemoForm')

from django import forms
from django.utils.translation import ugettext_lazy as _

from tinymce.widgets import TinyMCE

from dash.base import DashboardPluginFormBase

class MemoForm(forms.Form, DashboardPluginFormBase):
    """
    Memo form (for ``Memo`` plugin).
    """
    plugin_data_fields = [
        ("title", ""),
        ("text", "")
    ]

    title = forms.CharField(label=_("Title"), required=False)
    text = forms.CharField(label=_("Text"), required=True, widget=forms.widgets.Textarea)

# Basic TinyMCE config
mce_attrs = {
    'plugins': 'visualchars,paste',
    'theme': 'advanced',
    'theme_advanced_buttons1': 'formatselect,|,bold,italic,underline,|,bullist,numlist',
    'theme_advanced_buttons2': 'link,unlink,|,code',
    'width': '300',
    'delta_height': '150',
    'relative_urls': 0
}

class TinyMCEMemoForm(forms.Form, DashboardPluginFormBase):
    """
    TinyMCE memo form (for ``TinyMCEMemo`` plugin).
    """
    plugin_data_fields = [
        ("title", ""),
        ("text", "")
    ]

    title = forms.CharField(label=_("Title"), required=False)
    text = forms.CharField(label=_("HTML"), required=True, widget=TinyMCE(mce_attrs=mce_attrs))
