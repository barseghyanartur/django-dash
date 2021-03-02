from django import forms
from django.utils.translation import gettext_lazy as _

from ....base import DashboardPluginFormBase

try:
    from tinymce.widgets import TinyMCE
except ImportError:
    from ....lib.tinymce.widgets import TinyMCE

__title__ = 'dash.contrib.plugins.memo.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'MCE_ATTRS',
    'MemoForm',
    'TinyMCEMemoForm',
)


class MemoForm(forms.Form, DashboardPluginFormBase):
    """Memo form (for ``Memo`` plugin)."""

    plugin_data_fields = [
        ("title", ""),
        ("text", "")
    ]

    title = forms.CharField(label=_("Title"), required=False)
    text = forms.CharField(label=_("Text"), required=True,
                           widget=forms.widgets.Textarea)


# Basic TinyMCE config
MCE_ATTRS = {
    'plugins': 'visualchars,paste',
    'theme': 'advanced',
    'theme_advanced_buttons1':
        'formatselect,|,bold,italic,underline,|,bullist,numlist',
    'theme_advanced_buttons2': 'link,unlink,|,code',
    'width': '300',
    'delta_height': '150',
    'relative_urls': 0
}


class TinyMCEMemoForm(forms.Form, DashboardPluginFormBase):
    """TinyMCE memo form (for ``TinyMCEMemo`` plugin)."""

    plugin_data_fields = [
        ("title", ""),
        ("text", "")
    ]

    title = forms.CharField(label=_("Title"), required=False)
    text = forms.CharField(label=_("HTML"), required=True,
                           widget=TinyMCE(mce_attrs=MCE_ATTRS))
