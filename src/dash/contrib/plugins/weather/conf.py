from django.conf import settings

from . import defaults

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('get_setting',)


def get_setting(setting, override=None):
    """Get setting.

    Get a setting from ``dash.contrib.plugins.weather`` conf module, falling
    back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults to
        None.
    :return: Setting value.
    """
    attr_name = 'DASH_PLUGIN_WEATHER_{0}'.format(setting)
    if hasattr(settings, attr_name):
        return getattr(settings, attr_name)
    else:
        if hasattr(defaults, setting):
            return getattr(defaults, setting)
        else:
            return override
