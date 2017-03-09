from dash.contrib.plugins.weather.conf import get_setting

__title__ = 'dash.contrib.plugins.weather.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'API_ENDPOINT_URL',
    'API_KEY',
    'DEFAULT_CACHE_FOR',
    'DEFAULT_SHOW_TITLE',
)

API_KEY = get_setting('API_KEY')
API_ENDPOINT_URL = get_setting('API_ENDPOINT_URL')
DEFAULT_SHOW_TITLE = get_setting('DEFAULT_SHOW_TITLE')
DEFAULT_CACHE_FOR = get_setting('DEFAULT_CACHE_FOR')
