__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Video2x2AndroidMainWidget', 'Video3x3AndroidMainWidget', 'Video4x4AndroidMainWidget', \
           'Video5x5AndroidMainWidget', 'Video2x2Windows8MainWidget', 'Video2x2Windows8SidebarWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ****************** Android widgets for Video plugin ******************
# **********************************************************************

class Video2x2AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Video plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'video_2x2'
    cols = 2
    rows = 2
    media_css = (
        'css/dash_plugin_video.css',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('video/render_main.html', context)


# **********************************************************************
# ****************** Android widgets for Big video plugin **************
# **********************************************************************

class Video3x3AndroidMainWidget(Video2x2AndroidMainWidget):
    """
    Big video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'video_3x3'
    cols = 3
    rows = 3

# **********************************************************************
# ****************** Android widgets for Huge video plugin *************
# **********************************************************************

class Video4x4AndroidMainWidget(Video2x2AndroidMainWidget):
    """
    Huge video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'video_4x4'
    cols = 4
    rows = 4

# **********************************************************************
# ****************** Android widgets for Gigantic video plugin *********
# **********************************************************************

class Video5x5AndroidMainWidget(Video2x2AndroidMainWidget):
    """
    Gigantic video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'video_5x5'
    cols = 5
    rows = 5

# **********************************************************************
# ****************** Windows 8 widgets for Video plugin ****************
# **********************************************************************

class Video2x2Windows8MainWidget(BaseDashboardPluginWidget):
    """
    Video plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'video_2x2'
    cols = 2
    rows = 2
    media_css = (
        'css/dash_plugin_video.css',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('video/render_main.html', context)


class Video2x2Windows8SidebarWidget(Video2x2Windows8MainWidget):
    """
    Video plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
