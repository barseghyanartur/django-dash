__all__ = ('VideoAndroidMainWidget', 'BigVideoAndroidMainWidget', 'HugeVideoAndroidMainWidget', \
           'GiganticVideoAndroidMainWidget', 'VideoWindows8MainWidget', 'VideoWindows8SidebarWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ****************** Android widgets for Video plugin ******************
# **********************************************************************

class VideoAndroidMainWidget(BaseDashboardPluginWidget):
    """
    Video plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'video'
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

class BigVideoAndroidMainWidget(VideoAndroidMainWidget):
    """
    Big video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'big_video'
    cols = 3
    rows = 3

# **********************************************************************
# ****************** Android widgets for Huge video plugin *************
# **********************************************************************

class HugeVideoAndroidMainWidget(VideoAndroidMainWidget):
    """
    Huge video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'huge_video'
    cols = 4
    rows = 4

# **********************************************************************
# ****************** Android widgets for Gigantic video plugin *********
# **********************************************************************

class GiganticVideoAndroidMainWidget(VideoAndroidMainWidget):
    """
    Gigantic video plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'gigantic_video'
    cols = 5
    rows = 5

# **********************************************************************
# ****************** Windows 8 widgets for Video plugin ****************
# **********************************************************************

class VideoWindows8MainWidget(BaseDashboardPluginWidget):
    """
    Video plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'video'
    cols = 2
    rows = 2
    media_css = (
        'css/dash_plugin_video.css',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('video/render_main.html', context)


class VideoWindows8SidebarWidget(VideoWindows8MainWidget):
    """
    Video plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
