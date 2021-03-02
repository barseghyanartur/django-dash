from django.template.loader import render_to_string

from ....base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseVideoWidget',
    'Video1x1Widget',
    'Video2x2Widget',
    'Video3x3Widget',
    'Video4x4Widget',
    'Video5x5Widget'
)

# **********************************************************************
# *********************** Base Video widget plugin *********************
# **********************************************************************


class BaseVideoWidget(BaseDashboardPluginWidget):
    """Base video plugin widget."""

    media_css = (
        'css/dash_plugin_video.css',
    )

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('video/render.html', context)

# **********************************************************************
# ************************** Specific widgets **************************
# **********************************************************************


class Video1x1Widget(BaseVideoWidget):
    """Video plugin 1x1 widget."""

    plugin_uid = 'video_1x1'


class Video2x2Widget(BaseVideoWidget):
    """Video plugin 2x2 widget."""

    plugin_uid = 'video_2x2'
    cols = 2
    rows = 2


class Video3x3Widget(BaseVideoWidget):
    """Video plugin 3x3 widget."""

    plugin_uid = 'video_3x3'
    cols = 3
    rows = 3


class Video4x4Widget(BaseVideoWidget):
    """Video plugin 4x4 widget."""

    plugin_uid = 'video_4x4'
    cols = 4
    rows = 4


class Video5x5Widget(BaseVideoWidget):
    """Video plugin 5x5 widget."""

    plugin_uid = 'video_5x5'
    cols = 5
    rows = 5
