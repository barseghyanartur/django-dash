__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('WeatherForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from pif import get_public_ip

from dash.base import DashboardPluginFormBase
from dash.widgets import BooleanRadioSelect
from dash.contrib.plugins.rss_feed.defaults import DEFAULT_SHOW_TITLE, DEFAULT_CACHE_FOR

import logging
logger = logging.getLogger(__name__)

class WeatherForm(forms.Form, DashboardPluginFormBase):
    """
    Form for main ``WeatherPlugin``.
    """
    plugin_data_fields = [
        ("custom_title", ""),
        ("show_title", DEFAULT_SHOW_TITLE),
        ("cache_for", DEFAULT_CACHE_FOR),
        ("public_ip", ""),
        ("weather_data_json", "")

    ]
    custom_title = forms.CharField(label=_("Custom title"), required=False)
    show_feed_title = forms.BooleanField(label=_("Show title?"), required=False, initial=DEFAULT_SHOW_TITLE, \
                                         widget=BooleanRadioSelect)
    cache_for = forms.IntegerField(label=_("Cache for"), required=True, initial=DEFAULT_CACHE_FOR)
    public_ip = forms.CharField(label=_("Public IP"), required=False, widget=forms.widgets.HiddenInput)
    weather_data_json = forms.CharField(label=_("Weather data JSON"), required=False, widget=forms.widgets.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)

    def save_plugin_data(self, request=None):
        """
        For showing the weather, we need an IP address. Although we don't make it possible for the user to
        specify it manually, we silently obtain it and save into the plugin data.
        """
        if not self.cleaned_data.get('public_ip', None):
            try:
                self.cleaned_data['public_ip'] = get_public_ip()
            except Exception as e:
                if DEBUG:
                    logger.debug(e)
