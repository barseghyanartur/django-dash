__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseReadRSSFeedWidget', 'ReadRSSFeed2x3Widget', 'ReadRSSFeed3x3Widget')

from django.core.context_processors import csrf
from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************

class BaseReadRSSFeedWidget(BaseDashboardPluginWidget):
    """
    Base read RSS feed plugin widget.
    """
    media_js = [
        'js/dash_plugin_read_rss_feed.js',
    ]
    media_css = [
        'css/dash_plugin_read_rss_feed.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin, 'csrfmiddlewaretoken': csrf(request)}
        return render_to_string('rss_feed/render.html', context)

# ***********************************************************************
# ********************** Specific widgets for Memo plugin ***************
# ***********************************************************************

class ReadRSSFeed2x3Widget(BaseReadRSSFeedWidget):
    """
    Read RSS feed 2x3 plugin widget.
    """
    plugin_uid = 'read_rss_feed_2x3'
    cols = 2
    rows = 3


class ReadRSSFeed3x3Widget(BaseReadRSSFeedWidget):
    """
    Big read RSS 3x3 feed plugin widget.
    """
    plugin_uid = 'read_rss_feed_3x3'
    cols = 3
    rows = 3
