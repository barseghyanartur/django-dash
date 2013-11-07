__all__ = ('ReadRSSFeed2x3Plugin', 'ReadRSSFeed3x3Plugin')

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.rss_feed.forms import ReadRSSFeedForm
from dash.contrib.plugins.rss_feed.dash_widgets import (
    ReadRSSFeed2x3AndroidMainWidget, ReadRSSFeed2x3Windows8MainWidget, ReadRSSFeed3x3AndroidMainWidget
    )

# ***************************************************************************
# ******************************* Read RSS feed plugin **********************
# ***************************************************************************

class ReadRSSFeed2x3Plugin(BaseDashboardPlugin):
    """
    Read RSS feed into HTML plugin.
    """
    uid = 'read_rss_feed_2x3'
    name = _("Read RSS feed")
    form = ReadRSSFeedForm
    group = _("Internet")

plugin_registry.register(ReadRSSFeed2x3Plugin)

# ***************************************************************************
# ******************************* Read RSS feed plugin **********************
# ***************************************************************************

class ReadRSSFeed3x3Plugin(ReadRSSFeed2x3Plugin):
    """
    Big read RSS feed into HTML plugin.
    """
    uid = 'read_rss_feed_3x3'
    name = _("Read RSS feed")

plugin_registry.register(ReadRSSFeed3x3Plugin)

# *************************************************************************
# ****************** Registering the widgets ******************************
# *************************************************************************

# Registering the Android widgets for Read RSS feed plugin plugin.
plugin_widget_registry.register(ReadRSSFeed2x3AndroidMainWidget)
plugin_widget_registry.register(ReadRSSFeed3x3AndroidMainWidget)

# Registering the Windows8 widgets for Read RSS feed plugin.
plugin_widget_registry.register(ReadRSSFeed2x3Windows8MainWidget)
