__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('API_KEY', 'API_ENDPOINT_URL', 'DEFAULT_SHOW_TITLE', 'DEFAULT_CACHE_FOR')

from dash.contrib.plugins.weather.conf import get_setting

API_KEY = get_setting('API_KEY')
API_ENDPOINT_URL = get_setting('API_ENDPOINT_URL')
DEFAULT_SHOW_TITLE = get_setting('DEFAULT_SHOW_TITLE')
DEFAULT_CACHE_FOR = get_setting('DEFAULT_CACHE_FOR')
