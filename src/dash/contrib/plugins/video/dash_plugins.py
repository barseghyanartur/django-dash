from django.utils.translation import gettext_lazy as _

from vishap import render_video

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory

from .forms import VideoForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BaseVideoPlugin',)


# ***************************************************************************
# ******************************* Base Video plugin *************************
# ***************************************************************************


class BaseVideoPlugin(BaseDashboardPlugin):
    """Base Video plugin."""

    name = _("Video")
    group = _("Internet")
    form = VideoForm
    html_classes = ['video']

    def post_processor(self):
        """Post process."""
        self.data.embed_code = render_video(self.data.url)

# ***************************************************************************
# ********** Generating and registering the plugins using factory ***********
# ***************************************************************************


sizes = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6)
)

plugin_factory(BaseVideoPlugin, 'video', sizes)
