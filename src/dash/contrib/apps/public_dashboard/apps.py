try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'dash.contrib.apps.public_dashboard'
        label = 'dash_contrib_apps_public_dashboard'

except ImportError:
    pass

__title__ = 'dash.contrib.apps.public_dashboard.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)
