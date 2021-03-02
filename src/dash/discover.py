import logging
import sys

from django.utils.module_loading import autodiscover_modules

from .conf import get_setting

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('autodiscover',)

logger = logging.getLogger(__file__)

# In Django a dotted path can be used up to the app config class.


def autodiscover():
    """Auto-discovers files that should be found by dash."""
    # For Python 3 we need to increase the recursion limit, otherwise things
    # break. What we want is to set the recursion limit back to its' initial
    # value after all plugins have been discovered.
    recursion_limit = 1500
    default_recursion_limit = sys.getrecursionlimit()

    if recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(recursion_limit)

    PLUGINS_MODULE_NAME = get_setting('PLUGINS_MODULE_NAME')
    LAYOUTS_MODULE_NAME = get_setting('LAYOUTS_MODULE_NAME')

    # Discover plugins
    autodiscover_modules(PLUGINS_MODULE_NAME)

    # Discover layouts
    autodiscover_modules(LAYOUTS_MODULE_NAME)

    if recursion_limit > default_recursion_limit:
        sys.setrecursionlimit(default_recursion_limit)
