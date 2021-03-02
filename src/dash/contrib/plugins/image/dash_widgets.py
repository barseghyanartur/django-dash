from django.conf import settings
from django.template.loader import render_to_string

from ....base import BaseDashboardPluginWidget

from .helpers import get_crop_filter
from .settings import FIT_METHOD_FIT_WIDTH, FIT_METHOD_FIT_HEIGHT

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseImageWidget',
    'Image1x1Widget',
    'Image1x2Widget',
    'Image2x1Widget',
    'Image2x2Widget',
    'Image2x3Widget',
    'Image3x2Widget',
    'Image3x3Widget',
    'Image3x4Widget',
    'Image4x3Widget',
    'Image4x4Widget',
    'Image4x5Widget',
    'Image5x4Widget',
    'Image5x5Widget',
)

# **********************************************************************
# ************************ Base Image widget plugin ********************
# **********************************************************************


class BaseImageWidget(BaseDashboardPluginWidget):
    """Base image plugin widget."""

    media_js = (
        'js/dash_plugin_image.js',
    )
    media_css = (
        'css/dash_plugin_image.css',
    )

    def render(self, request=None):
        """Render."""
        crop = get_crop_filter(self.plugin.data.fit_method)
        # Widget size with 8px cropped in width and height.
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
            'thumb_size': 'x'.join([str(_val) for _val in thumb_size])
        }
        return render_to_string('image/render.html', context)

# **********************************************************************
# ************************** Specific widgets **************************
# **********************************************************************


class Image1x1Widget(BaseImageWidget):
    """Image1x1 plugin widget."""

    plugin_uid = 'image_1x1'


class Image1x2Widget(BaseImageWidget):
    """Image1x2 plugin widget."""

    cols = 1
    rows = 2
    plugin_uid = 'image_1x2'


class Image2x1Widget(BaseImageWidget):
    """Image2x1 plugin widget."""

    cols = 2
    rows = 1
    plugin_uid = 'image_2x1'


class Image2x2Widget(BaseImageWidget):
    """Image2x2 plugin widget."""

    cols = 2
    rows = 2
    plugin_uid = 'image_2x2'


class Image2x3Widget(BaseImageWidget):
    """Image2x3 plugin widget."""

    cols = 2
    rows = 3
    plugin_uid = 'image_2x3'


class Image3x2Widget(BaseImageWidget):
    """Image3x2 plugin widget."""

    cols = 3
    rows = 2
    plugin_uid = 'image_3x2'


class Image3x3Widget(BaseImageWidget):
    """Image3x3 plugin widget."""

    cols = 3
    rows = 3
    plugin_uid = 'image_3x3'


class Image3x4Widget(BaseImageWidget):
    """Image3x4 plugin widget."""

    cols = 3
    rows = 4
    plugin_uid = 'image_3x4'


class Image4x3Widget(BaseImageWidget):
    """Image4x3 plugin widget."""

    cols = 4
    rows = 3
    plugin_uid = 'image_4x3'


class Image4x4Widget(BaseImageWidget):
    """Image4x4 plugin widget."""

    cols = 4
    rows = 4
    plugin_uid = 'image_4x4'


class Image4x5Widget(BaseImageWidget):
    """Image4x5 plugin widget."""

    cols = 4
    rows = 5
    plugin_uid = 'image_4x5'


class Image5x4Widget(BaseImageWidget):
    """Image5x4 plugin widget."""

    cols = 5
    rows = 4
    plugin_uid = 'image_5x4'


class Image5x5Widget(BaseImageWidget):
    """Image5x5 plugin widget."""

    cols = 5
    rows = 5
    plugin_uid = 'image_5x5'
