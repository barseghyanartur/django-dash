from django.apps import AppConfig

__title__ = 'dash.contrib.plugins.image.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'dash.contrib.plugins.image'
    label = 'dash_contrib_plugins_image'
