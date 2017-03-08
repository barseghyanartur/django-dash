try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'dash.contrib.plugins.url'
        label = 'dash_contrib_plugins_url'

except ImportError:
    pass

__title__ = 'dash.contrib.plugins.url.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)
