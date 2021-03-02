from django import forms
from django.utils.translation import gettext_lazy as _

from dash.base import DashboardPluginFormBase

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'


class ChartForm(forms.Form, DashboardPluginFormBase):
    """Chart form for `ChartBasePlugin` plugin."""

    plugin_data_fields = [
        ("title", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
