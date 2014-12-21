__title__ = 'dash.discover'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

import imp

from django.conf import settings

from dash.conf import get_setting

def autodiscover():
    """
    Autodiscovers files that should be found by dash.
    """
    PLUGINS_MODULE_NAME = get_setting('PLUGINS_MODULE_NAME')
    LAYOUTS_MODULE_NAME = get_setting('LAYOUTS_MODULE_NAME')

    def do_discover(module_name):
        for app in settings.INSTALLED_APPS:
            try:
                app = str(app)
                app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
            except (AttributeError, TypeError) as e:
                continue

            try:
                imp.find_module(module_name, app_path)
            except ImportError:
                continue
            __import__('{0}.{1}'.format(app, module_name))

    # Discover layouts
    do_discover(LAYOUTS_MODULE_NAME)

    # Discover plugins
    do_discover(PLUGINS_MODULE_NAME)
