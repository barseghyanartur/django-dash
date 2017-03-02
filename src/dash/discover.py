import imp
import logging
import sys

import six

from django.conf import settings

from nine.versions import DJANGO_GTE_1_7

from .conf import get_setting

__title__ = 'dash.discover'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('autodiscover',)

logger = logging.getLogger(__file__)

# In Django a dotted path can be used up to the app config class. In
# such cases the old-school auto-discovery of modules doesn't work but we
# have a great Django `autodiscover_modules` tool then. In cases if Django
# version is >= 1.7, we use the Django `autodiscover_modules` tool falling back
# to our own implementation of it otherwise.
if DJANGO_GTE_1_7:
    from django.utils.module_loading import autodiscover_modules
else:
    def autodiscover_modules(module_name):
        for app in settings.INSTALLED_APPS:
            try:
                app = str(app)
                app_path = __import__(
                    app,
                    {},
                    {},
                    [app.split('.')[-1]]
                ).__path__
            except (AttributeError, TypeError) as e:
                logger.debug(str(e))
                continue

            try:
                imp.find_module(module_name, app_path)
            except ImportError as e:
                logger.debug(str(e))
                continue
            __import__('{0}.{1}'.format(app, module_name))


def autodiscover():
    """Auto-discovers files that should be found by dash."""
    # For Python 3 we need to increase the recursion limit, otherwise things
    # break. What we want is to set the recursion limit back to its' initial
    # value after all plugins have been discovered.
    recursion_limit = 1500
    default_recursion_limit = sys.getrecursionlimit()

    if six.PY3 and recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(recursion_limit)

    PLUGINS_MODULE_NAME = get_setting('PLUGINS_MODULE_NAME')
    LAYOUTS_MODULE_NAME = get_setting('LAYOUTS_MODULE_NAME')

    # Discover plugins
    autodiscover_modules(PLUGINS_MODULE_NAME)

    # Discover layouts
    autodiscover_modules(LAYOUTS_MODULE_NAME)

    if six.PY3 and recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(default_recursion_limit)
