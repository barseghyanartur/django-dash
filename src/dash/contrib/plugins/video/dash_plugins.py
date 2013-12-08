__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseVideoPlugin',)

from django.utils.translation import ugettext_lazy as _

from vishap import render_video

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory
from dash.contrib.plugins.video.forms import VideoForm

# ********************************************************************************
# ******************************* Base Video plugin ******************************
# ********************************************************************************

class BaseVideoPlugin(BaseDashboardPlugin):
    """
    Base Video plugin.
    """
    name = _("Video")
    group = _("Internet")
    form = VideoForm
    html_classes = ['video']

    def post_processor(self):
        self.data.embed_code = render_video(self.data.url)

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************

sizes = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6)
)

plugin_factory(BaseVideoPlugin, 'video', sizes)
