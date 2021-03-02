from django.apps import AppConfig

__title__ = 'dash.contrib.plugins.memo.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'dash.contrib.plugins.memo'
    label = 'dash_contrib_plugins_memo'
