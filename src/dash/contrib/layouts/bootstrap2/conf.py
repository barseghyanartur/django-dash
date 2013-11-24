__all__ = ('get_setting',)

from django.conf import settings

from dash.contrib.layouts.bootstrap2 import defaults

def get_setting(setting, override=None):
    """
    Get a setting from ``dash.contrib.layouts.bootstrap2`` conf module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults to None.
    :return: Setting value.
    """
    if override is not None:
        return override
    if hasattr(settings, 'DASH_LAYOUT_BOOTSTRAP2_{0}'.format(setting)):
        return getattr(settings, 'DASH_LAYOUT_BOOTSTRAP2_{0}'.format(setting))
    else:
        return getattr(defaults, setting)
