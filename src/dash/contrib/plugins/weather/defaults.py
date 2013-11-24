__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('API_KEY', 'API_ENDPOINT_URL', 'DEFAULT_SHOW_TITLE', 'DEFAULT_CACHE_FOR')

# http://developer.worldweatheronline.com API key.
API_KEY = ''

# Endpoing URL for the weather API. Should get (key, format, q) arguments.
API_ENDPOINT_URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx?key={0}&format={1}&q={2}'

DEFAULT_SHOW_TITLE = True

DEFAULT_CACHE_FOR = 3600
