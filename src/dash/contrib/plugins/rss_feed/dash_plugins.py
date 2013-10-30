__all__ = ('ReadRSSFeedPlugin', 'BigReadRSSFeedPlugin')

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.rss_feed.forms import ReadRSSFeedForm
from dash.contrib.plugins.rss_feed.dash_widgets import ReadRSSFeedAndroidMainWidget, ReadRSSFeedWindows8MainWidget
from dash.contrib.plugins.rss_feed.dash_widgets import BigReadRSSFeedAndroidMainWidget

# ***************************************************************************
# ******************************* Read RSS feed plugin **********************
# ***************************************************************************

class ReadRSSFeedPlugin(BaseDashboardPlugin):
    """
    Read RSS feed into HTML plugin.
    """
    uid = 'read_rss_feed'
    name = _("Read RSS feed")
    form = ReadRSSFeedForm
    group = _("Internet")

plugin_registry.register(ReadRSSFeedPlugin)

# ***************************************************************************
# ******************************* Read RSS feed plugin **********************
# ***************************************************************************

class BigReadRSSFeedPlugin(ReadRSSFeedPlugin):
    """
    Big read RSS feed into HTML plugin.
    """
    uid = 'big_read_rss_feed'
    name = _("Read RSS feed")

plugin_registry.register(BigReadRSSFeedPlugin)

# *************************************************************************
# ****************** Registering the widgets ******************************
# *************************************************************************

# Registering the Android widgets for Read RSS feed plugin plugin.
plugin_widget_registry.register(ReadRSSFeedAndroidMainWidget)
plugin_widget_registry.register(BigReadRSSFeedAndroidMainWidget)

# Registering the Windows8 widgets for Dummy plugin.
plugin_widget_registry.register(ReadRSSFeedWindows8MainWidget)
