import logging

from django import forms
from django.utils.translation import gettext_lazy as _

from pif import get_public_ip

from ....base import DashboardPluginFormBase
from ....widgets import BooleanRadioSelect

from .defaults import DEFAULT_CACHE_FOR, DEFAULT_SHOW_TITLE

__title__ = 'dash.contrib.plugins.weather.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('WeatherForm',)

logger = logging.getLogger(__name__)


class WeatherForm(forms.Form, DashboardPluginFormBase):
    """Form for main ``WeatherPlugin``."""

    plugin_data_fields = [
        ("custom_title", ""),
        ("show_title", DEFAULT_SHOW_TITLE),
        ("cache_for", DEFAULT_CACHE_FOR),
        ("public_ip", ""),
        ("weather_data_json", "")

    ]
    custom_title = forms.CharField(label=_("Custom title"), required=False)
    show_feed_title = forms.BooleanField(label=_("Show title?"),
                                         required=False,
                                         initial=DEFAULT_SHOW_TITLE,
                                         widget=BooleanRadioSelect)
    cache_for = forms.IntegerField(label=_("Cache for"),
                                   required=True,
                                   initial=DEFAULT_CACHE_FOR)
    public_ip = forms.CharField(label=_("Public IP"),
                                required=False,
                                widget=forms.widgets.HiddenInput)
    weather_data_json = forms.CharField(label=_("Weather data JSON"),
                                        required=False,
                                        widget=forms.widgets.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)

    def save_plugin_data(self, request=None):
        """Save plugin data.

        For showing the weather, we need an IP address. Although we don't
        make it possible for the user to specify it manually, we silently
        obtain it and save into the plugin data.
        """
        if not self.cleaned_data.get('public_ip', None):
            try:
                self.cleaned_data['public_ip'] = get_public_ip()
            except Exception as err:
                logger.debug(err)
