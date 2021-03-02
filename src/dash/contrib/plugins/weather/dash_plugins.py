import json
import logging
from urllib.request import urlopen

from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory
from ....settings import DEBUG

from .forms import WeatherForm
from .settings import API_KEY, API_ENDPOINT_URL

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BaseWeatherPlugin',)

logger = logging.getLogger(__name__)

# ***************************************************************************
# ************************** Base Weather plugin ****************************
# ***************************************************************************


class BaseWeatherPlugin(BaseDashboardPlugin):
    """Base Weather plugin."""

    name = _("Weather")
    form = WeatherForm
    group = _("Weather")

    def post_processor(self):
        """Post process.

        If no text available, use dummy.
        """
        key = '{0}-{1}-{2}'.format(self.layout_uid,
                                   self.placeholder_uid,
                                   self.uid)
        self.data.weather_data_json = cache.get(key)

        if not self.data.weather_data_json:

            if self.data.public_ip:
                api_endpoint_url = API_ENDPOINT_URL.format(
                    API_KEY,
                    'json',
                    self.data.public_ip
                )

                try:
                    data = str(urlopen(api_endpoint_url).read())

                    self.data.weather_data_json = json.loads(data)

                    cache.set(
                        key,
                        self.data.weather_data_json,
                        int(self.data.cache_for)
                    )
                except Exception as err:
                    if DEBUG:
                        logger.debug(err)

        if self.data.weather_data_json:
            data = self.data.weather_data_json['data']

            try:
                current_condition = data['current_condition'][0]
            except (KeyError, TypeError, IndexError):
                current_condition = None

            if current_condition:
                self.data.current_cloudcover = current_condition['cloudcover']
                self.data.current_humidity = current_condition['humidity']
                self.data.current_pressure = current_condition['pressure']
                self.data.current_visibility = current_condition['visibility']
                self.data.current_temp_c = current_condition['temp_C']

                try:
                    self.data.current_weather_desc = \
                        current_condition['weatherDesc'][0]['value']
                except (KeyError, TypeError, IndexError):
                    pass

                try:
                    self.data.current_weather_icon_url = \
                        current_condition['weatherIconUrl'][0]['value']
                except (KeyError, TypeError, IndexError):
                    pass

            try:
                weather = data['weather'][0]
            except (KeyError, TypeError, IndexError):
                weather = None

            if weather:
                self.data.temp_max_c = weather['tempMaxC']
                self.data.temp_min_c = weather['tempMinC']
                self.data.windspeed_kmph = weather['windspeedKmph']
                self.data.wind_dir_16_point = weather['winddir16Point']

                try:
                    self.data.weather_desc = weather['weatherDesc'][0]['value']
                except (KeyError, TypeError, IndexError):
                    pass

                try:
                    self.data.weather_icon_url = \
                        weather['weatherIconUrl'][0]['value']
                except (KeyError, TypeError, IndexError):
                    pass


# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************


sizes = (
    (2, 2),
    (3, 3),
)

plugin_factory(BaseWeatherPlugin, 'weather', sizes)
