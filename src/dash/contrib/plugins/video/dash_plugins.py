__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Video2x2Plugin', 'Video3x3Plugin', 'Video4x4Plugin', 'Video5x5Plugin')

from django.utils.translation import ugettext_lazy as _

from vishap import render_video

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.video.forms import VideoForm
from dash.contrib.plugins.video.dash_widgets import Video2x2AndroidMainWidget, Video3x3AndroidMainWidget
from dash.contrib.plugins.video.dash_widgets import Video4x4AndroidMainWidget, Video5x5AndroidMainWidget
from dash.contrib.plugins.video.dash_widgets import Video2x2Windows8MainWidget, Video2x2Windows8SidebarWidget

# *************************************************************************
# ******************************* Video plugin ****************************
# *************************************************************************

class Video2x2Plugin(BaseDashboardPlugin):
    """
    Video dashboard plugin.
    """
    uid = 'video_2x2'
    name = _("Video")
    group = _("Internet")
    form = VideoForm
    html_classes = ['video']

    def post_processor(self):
        self.data.embed_code = render_video(self.data.url)


plugin_registry.register(Video2x2Plugin)


# *************************************************************************
# ******************************* Big video plugin ************************
# *************************************************************************

class Video3x3Plugin(Video2x2Plugin):
    """
    Video dashboard plugin.
    """
    uid = 'video_3x3'
    name = _("Video")


plugin_registry.register(Video3x3Plugin)

# *************************************************************************
# ******************************* Huge video plugin ***********************
# *************************************************************************

class Video4x4Plugin(Video2x2Plugin):
    """
    Video dashboard plugin.
    """
    uid = 'video_4x4'
    name = _("Video")


plugin_registry.register(Video4x4Plugin)


# *************************************************************************
# ******************************* Gigantic video plugin *******************
# *************************************************************************

class Video5x5Plugin(Video2x2Plugin):
    """
    Video dashboard plugin.
    """
    uid = 'video_5x5'
    name = _("Video")


plugin_registry.register(Video5x5Plugin)

# *************************************************************************
# ****************** Registering the widgets for Video plugin *************
# *************************************************************************

# Registering the Android widgets for Video plugin.
plugin_widget_registry.register(Video2x2AndroidMainWidget)
plugin_widget_registry.register(Video3x3AndroidMainWidget)
plugin_widget_registry.register(Video4x4AndroidMainWidget)
plugin_widget_registry.register(Video5x5AndroidMainWidget)

# Registering the Windows8widgets for Video plugin.
plugin_widget_registry.register(Video2x2Windows8MainWidget)
plugin_widget_registry.register(Video2x2Windows8SidebarWidget)
