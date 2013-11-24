__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('VideoForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase
from dash.widgets import BooleanRadioSelect

class VideoForm(forms.Form, DashboardPluginFormBase):
    """
    Video form for ``VideoPlugin`` plugin.
    """
    plugin_data_fields = [
        ("title", ""),
        ("url", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
    url = forms.URLField(label=_("URL"), required=True)

