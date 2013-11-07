__all__ = ('Image1x1AndroidMainWidget', 'Image2x2AndroidMainWidget', 'Image3x3AndroidMainWidget',
           'Image3x2AndroidMainWidget', 'Image2x3AndroidMainWidget',
           'Image1x1Windows8MainWidget', 'Image1x1Windows8SidebarWidget')

from django.template.loader import render_to_string
from django.conf import settings

from dash.base import BaseDashboardPluginWidget
from dash.contrib.plugins.image.helpers import get_crop_filter
from dash.contrib.plugins.image.settings import FIT_METHOD_FIT_WIDTH, FIT_METHOD_FIT_HEIGHT

# **********************************************************************
# ****************** Android widgets for Image plugin ******************
# **********************************************************************

class Image1x1AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Image1x1 plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'image_1x1'
    cols = 1
    rows = 1
    media_js = (
        'js/dash_plugin_image.js',
    )
    media_css = (
        'css/dash_plugin_image.css',
    )

    def render(self, request=None):
        crop = get_crop_filter(self.plugin.data.fit_method)
        # Widget size with 8px bited from all width and height.
        if FIT_METHOD_FIT_WIDTH == self.plugin.data.fit_method:
            thumb_size = (self.get_width() - 8, 0)
        elif FIT_METHOD_FIT_HEIGHT == self.plugin.data.fit_method:
            thumb_size = (0, self.get_height() - 8)
        else:
            thumb_size = self.get_size(-8, -8)

        context = {
            'plugin': self.plugin,
            'MEDIA_URL': settings.MEDIA_URL,
            'crop': crop,
            'thumb_size': thumb_size
        }
        return render_to_string('image/render_main.html', context)

# ***************************************************************************
# ****************** Android widgets for Image2x2 plugin *******************
# ***************************************************************************

class Image2x2AndroidMainWidget(Image1x1AndroidMainWidget):
    """
    Image2x2 plugin widget for Android layout (placeholder `main`).
    """
    cols = 2
    rows = 2
    plugin_uid = 'image_2x2'

# ***************************************************************************
# ****************** Android widgets for Image3x3 plugin *******************
# ***************************************************************************

class Image3x3AndroidMainWidget(Image1x1AndroidMainWidget):
    """
    Image3x3 plugin widget for Android layout (placeholder `main`).
    """
    cols = 3
    rows = 3
    plugin_uid = 'image_3x3'

# ***************************************************************************
# ****************** Android widgets for Image3x2 plugin *******************
# ***************************************************************************

class Image3x2AndroidMainWidget(Image1x1AndroidMainWidget):
    """
    Image3x2 plugin widget for Android layout (placeholder `main`).
    """
    cols = 3
    rows = 2
    plugin_uid = 'image_3x2'

# ***************************************************************************
# ****************** Android widgets for Image2x3 plugin *******************
# ***************************************************************************

class Image2x3AndroidMainWidget(Image1x1AndroidMainWidget):
    """
    Image2x3 plugin widget for Android layout (placeholder `main`).
    """
    cols = 2
    rows = 3
    plugin_uid = 'image_2x3'

# **********************************************************************
# ****************** Windows 8 widgets for Image plugin ****************
# **********************************************************************

class Image1x1Windows8MainWidget(Image1x1AndroidMainWidget):
    """
    Image1x1 plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'image_1x1'
    cols = 1
    rows = 1


class Image1x1Windows8SidebarWidget(Image1x1Windows8MainWidget):
    """
    Image plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
