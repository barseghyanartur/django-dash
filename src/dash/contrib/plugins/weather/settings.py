__all__ = ('API_KEY', 'API_ENDPOINT_URL', 'DEFAULT_SHOW_TITLE', 'DEFAULT_CACHE_FOR')

from dash.contrib.plugins.weather.conf import get_setting

API_KEY = get_setting('API_KEY')
API_ENDPOINT_URL = get_setting('API_ENDPOINT_URL')
DEFAULT_SHOW_TITLE = get_setting('DEFAULT_SHOW_TITLE')
DEFAULT_CACHE_FOR = get_setting('DEFAULT_CACHE_FOR')
