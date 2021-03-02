__title__ = 'dash.contrib.plugins.weather.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'API_ENDPOINT_URL',
    'API_KEY',
    'DEFAULT_CACHE_FOR',
    'DEFAULT_SHOW_TITLE',
)

# http://developer.worldweatheronline.com API key.
API_KEY = ''

# Endpoint URL for the weather API. Should get (key, format, q) arguments.
API_ENDPOINT_URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx' \
                   '?key={0}&format={1}&q={2}'

DEFAULT_SHOW_TITLE = True

DEFAULT_CACHE_FOR = 3600
