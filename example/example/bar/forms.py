__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase

from bar.defaults import DEFAULT_DATE_VALUE, DEFAULT_OPEN_VALUE

class ChartForm(forms.Form, DashboardPluginFormBase):
    """
    Chart form for `ChartBasePlugin` plugin.
    """

    plugin_data_fields = [
        ("title", ""),
        ("data_date", DEFAULT_DATE_VALUE),
        ("data_open", DEFAULT_OPEN_VALUE)
    ]

    title = forms.CharField(label=_("Title"), required=True)
    data_date = forms.CharField(label=_("Date"), required=True, initial=DEFAULT_DATE_VALUE,
                                widget=forms.widgets.Textarea)
    data_open = forms.CharField(label=_("Open"), required=True, initial=DEFAULT_OPEN_VALUE,
                                widget=forms.widgets.Textarea)
