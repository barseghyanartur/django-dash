try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'dash.contrib.plugins.rss_feed'
        label = 'dash_contrib_plugins_rss_feed'

except ImportError:
    pass

__title__ = 'dash.contrib.plugins.rss_feed.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)
