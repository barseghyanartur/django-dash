JSON_PACKAGE_USED = None
# Experimental switch to ujson
try:
    import ujson as json
    JSON_PACKAGE_USED = 'ujson'
except ImportError as e:
    try:
        import simplejson as json
        JSON_PACKAGE_USED = 'simplejson'
    except ImportError as e:
        import json
        JSON_PACKAGE_USED = 'json'

__title__ = 'dash.json_package'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'json',
    'JSON_PACKAGE_USED',
)
