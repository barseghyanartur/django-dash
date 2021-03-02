from django.apps import AppConfig

__title__ = 'dash.contrib.plugins.dummy.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Config',)


class Config(AppConfig):
    name = 'dash.contrib.plugins.dummy'
    label = 'dash_contrib_plugins_dummy'
