__all__ = ('ReadRSSFeed2x3AndroidMainWidget', 'ReadRSSFeed2x3Windows8MainWidget', 'ReadRSSFeed3x3AndroidMainWidget')

from django.core.context_processors import csrf
from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************
class ReadRSSFeed2x3AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Read RSS feed plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'read_rss_feed_2x3'
    cols = 2
    rows = 3

    media_js = [
        'js/dash_plugin_read_rss_feed.js',
    ]
    media_css = [
        'css/dash_plugin_read_rss_feed.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin, 'csrfmiddlewaretoken': csrf(request)}
        return render_to_string('rss_feed/render_main.html', context)

# ************************************************************************
# ****************** Android widgets for Big read RSS feed plugin ********
# ************************************************************************
class ReadRSSFeed3x3AndroidMainWidget(ReadRSSFeed2x3AndroidMainWidget):
    """
    Big read RSS feed plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'read_rss_feed_3x3'
    cols = 3
    rows = 3


# ************************************************************************
# ****************** Windows8 widgets for Read RSS feed plugin ***********
# ************************************************************************
class ReadRSSFeed2x3Windows8MainWidget(ReadRSSFeed2x3AndroidMainWidget):
    """
    Read RSS feed plugin widget for Windows8 (placeholder `main`).
    """
    layout_uid = 'windows8'
