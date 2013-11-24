__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Weather2x2Plugin', 'Weather3x3Plugin')

from six.moves.urllib.request import urlopen
import json

from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.weather.forms import WeatherForm
from dash.contrib.plugins.weather.dash_widgets import Weather2x2AndroidMainWidget, Weather3x3AndroidMainWidget
from dash.contrib.plugins.weather.settings import API_KEY, API_ENDPOINT_URL
from dash.settings import DEBUG

import logging
logger = logging.getLogger(__name__)

# ***************************************************************************
# ******************************* Weather plugin ****************************
# ***************************************************************************

class Weather2x2Plugin(BaseDashboardPlugin):
    """
    Weather dashboard plugin.
    """
    uid = 'weather'
    name = _("Weather")
    form = WeatherForm
    group = _("Weather")

    def post_processor(self):
        """
        If no text available, use dummy.
        """
        key = '{0}-{1}-{2}'.format(self.layout_uid, self.placeholder_uid, self.uid)
        self.data.weather_data_json = cache.get(key)

        if not self.data.weather_data_json:

            if self.data.public_ip:
                api_endpoint_url = API_ENDPOINT_URL.format(API_KEY, 'json', self.data.public_ip)

                try:
                    data = str(urlopen(api_endpoint_url).read())

                    self.data.weather_data_json = json.loads(data)

                    cache.set(key, self.data.weather_data_json, int(self.data.cache_for))
                except Exception as e:
                    if DEBUG:
                        logger.debug(e)

        if self.data.weather_data_json:
            data = self.data.weather_data_json['data']

            try:
                current_condition = data['current_condition'][0]
            except:
                current_condition = None

            if current_condition:
                self.data.current_cloudcover = current_condition['cloudcover']
                self.data.current_humidity = current_condition['humidity']
                self.data.current_pressure = current_condition['pressure']
                self.data.current_visibility = current_condition['visibility']
                self.data.current_temp_c = current_condition['temp_C']

                try:
                    self.data.current_weather_desc = current_condition['weatherDesc'][0]['value']
                except Exception as e:
                    pass

                try:
                    self.data.current_weather_icon_url = current_condition['weatherIconUrl'][0]['value']
                except Exception as e:
                    pass

            try:
                weather = data['weather'][0]
            except:
                weather = None

            if weather:
                self.data.temp_max_c = weather['tempMaxC']
                self.data.temp_min_c = weather['tempMinC']
                self.data.windspeed_kmph = weather['windspeedKmph']
                self.data.wind_dir_16_point = weather['winddir16Point']

                try:
                    self.data.weather_desc = weather['weatherDesc'][0]['value']
                except Exception as e:
                    pass

                try:
                    self.data.weather_icon_url = weather['weatherIconUrl'][0]['value']
                except Exception as e:
                    pass


plugin_registry.register(Weather2x2Plugin)

# ********************************************************************************
# ******************************* Big weather plugin *****************************
# ********************************************************************************

class Weather3x3Plugin(Weather2x2Plugin):
    """
    Big weather dashboard plugin.
    """
    uid = 'weather_3x3'
    name = _("Weather")
    group = _("Weather")


plugin_registry.register(Weather3x3Plugin)

# ********************************************************************************
# ******************************* Registering the widgets ************************
# ********************************************************************************

# Registering the Android widgets for Weather plugin.
plugin_widget_registry.register(Weather2x2AndroidMainWidget)

# Registering the Android widgets for Big weather plugin.
plugin_widget_registry.register(Weather3x3AndroidMainWidget)
