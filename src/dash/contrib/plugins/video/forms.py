from django import forms
from django.utils.translation import gettext_lazy as _

from ....base import DashboardPluginFormBase

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('VideoForm',)


class VideoForm(forms.Form, DashboardPluginFormBase):
    """Video form for ``VideoPlugin`` plugin."""

    plugin_data_fields = [
        ("title", ""),
        ("url", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
    url = forms.URLField(label=_("URL"), required=True)
