from django.template.loader import render_to_string

from nine import versions

from ....base import BaseDashboardPluginWidget

if versions.DJANGO_GTE_1_8:
    from django.template.context_processors import csrf
else:
    from django.core.context_processors import csrf

__title__ = 'dash.contrib.plugins.rss_feed.dash_widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseReadRSSFeedWidget',
    'ReadRSSFeed2x3Widget',
    'ReadRSSFeed3x3Widget',
)

# ************************************************************************
# ****************** Android widgets for Read RSS feed plugin ************
# ************************************************************************


class BaseReadRSSFeedWidget(BaseDashboardPluginWidget):
    """Base read RSS feed plugin widget."""

    media_js = [
        'js/dash_plugin_read_rss_feed.js',
    ]
    media_css = [
        'css/dash_plugin_read_rss_feed.css',
    ]

    def render(self, request=None):
        """Render."""
        context = {
            'plugin': self.plugin,
            'csrfmiddlewaretoken': csrf(request)
        }
        return render_to_string('rss_feed/render.html', context)

# ***********************************************************************
# ********************** Specific widgets for Memo plugin ***************
# ***********************************************************************


class ReadRSSFeed2x3Widget(BaseReadRSSFeedWidget):
    """Read RSS feed 2x3 plugin widget."""

    plugin_uid = 'read_rss_feed_2x3'
    cols = 2
    rows = 3


class ReadRSSFeed3x3Widget(BaseReadRSSFeedWidget):
    """Big read RSS 3x3 feed plugin widget."""

    plugin_uid = 'read_rss_feed_3x3'
    cols = 3
    rows = 3
