__all__ = ('VideoPlugin', 'BigVideoPlugin', 'HugeVideoPlugin', 'GiganticVideoPlugin')

from django.utils.translation import ugettext_lazy as _

from vishap import render_video

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.video.forms import VideoForm
from dash.contrib.plugins.video.dash_widgets import VideoAndroidMainWidget, BigVideoAndroidMainWidget
from dash.contrib.plugins.video.dash_widgets import HugeVideoAndroidMainWidget, GiganticVideoAndroidMainWidget
from dash.contrib.plugins.video.dash_widgets import VideoWindows8MainWidget, VideoWindows8SidebarWidget

# *************************************************************************
# ******************************* Video plugin ****************************
# *************************************************************************

class VideoPlugin(BaseDashboardPlugin):
    """
    Video dashboard plugin.
    """
    uid = 'video'
    name = _("Video")
    group = _("Internet")
    form = VideoForm

    @property
    def html_class(self):
        """
        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(VideoPlugin, self).html_class
        html_class += ' video'
        return html_class

    def post_processor(self):
        self.data.embed_code = render_video(self.data.url)


plugin_registry.register(VideoPlugin)


# *************************************************************************
# ******************************* Big video plugin ************************
# *************************************************************************

class BigVideoPlugin(VideoPlugin):
    """
    Video dashboard plugin.
    """
    uid = 'big_video'
    name = _("Video")


plugin_registry.register(BigVideoPlugin)

# *************************************************************************
# ******************************* Huge video plugin ***********************
# *************************************************************************

class HugeVideoPlugin(VideoPlugin):
    """
    Video dashboard plugin.
    """
    uid = 'huge_video'
    name = _("Video")


plugin_registry.register(HugeVideoPlugin)


# *************************************************************************
# ******************************* Gigantic video plugin *******************
# *************************************************************************

class GiganticVideoPlugin(VideoPlugin):
    """
    Video dashboard plugin.
    """
    uid = 'gigantic_video'
    name = _("Video")


plugin_registry.register(GiganticVideoPlugin)

# *************************************************************************
# ****************** Registering the widgets for Video plugin *************
# *************************************************************************

# Registering the Android widgets for Video plugin.
plugin_widget_registry.register(VideoAndroidMainWidget)
plugin_widget_registry.register(BigVideoAndroidMainWidget)
plugin_widget_registry.register(HugeVideoAndroidMainWidget)
plugin_widget_registry.register(GiganticVideoAndroidMainWidget)

# Registering the Windows8widgets for Video plugin.
plugin_widget_registry.register(VideoWindows8MainWidget)
plugin_widget_registry.register(VideoWindows8SidebarWidget)
