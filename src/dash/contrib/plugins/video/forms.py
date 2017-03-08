from django import forms
from django.utils.translation import ugettext_lazy as _

from ....base import DashboardPluginFormBase
from ....widgets import BooleanRadioSelect

__title__ = 'dash.contrib.plugins.video.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('VideoForm',)


class VideoForm(forms.Form, DashboardPluginFormBase):
    """Video form for ``VideoPlugin`` plugin."""

    plugin_data_fields = [
        ("title", ""),
        ("url", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
    url = forms.URLField(label=_("URL"), required=True)
