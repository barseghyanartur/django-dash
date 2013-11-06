__all__ = ('ImageAndroidMainWidget', 'ImageWindows8MainWidget', 'ImageWindows8SidebarWidget')

from django.template.loader import render_to_string
from django.conf import settings

from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ****************** Android widgets for Image plugin ******************
# **********************************************************************

class ImageAndroidMainWidget(BaseDashboardPluginWidget):
    """
    Image plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'image'
    cols = 1
    rows = 1
    media_js = (
        'js/dash_plugin_image.js',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin, 'MEDIA_URL': settings.MEDIA_URL}
        return render_to_string('image/render_main.html', context)


# **********************************************************************
# ****************** Windows 8 widgets for Image plugin ****************
# **********************************************************************

class ImageWindows8MainWidget(BaseDashboardPluginWidget):
    """
    Image plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'image'
    cols = 1
    rows = 1
    media_js = (
        'js/dash_plugin_image.js',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin, 'MEDIA_URL': settings.MEDIA_URL}
        return render_to_string('image/render_main.html', context)


class ImageWindows8SidebarWidget(ImageWindows8MainWidget):
    """
    Image plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
