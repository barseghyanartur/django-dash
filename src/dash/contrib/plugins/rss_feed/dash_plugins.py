from django.utils.translation import gettext_lazy as _

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory

from .forms import ReadRSSFeedForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BaseReadRSSFeedPlugin',)

# ****************************************************************************
# ********************************* Base Read RSS feed plugin ****************
# ****************************************************************************


class BaseReadRSSFeedPlugin(BaseDashboardPlugin):
    """Base Read RSS feed into HTML plugin."""

    name = _("Read RSS feed")
    form = ReadRSSFeedForm
    group = _("Internet")

# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************


sizes = (
    (2, 3),
    (3, 3),
)

plugin_factory(BaseReadRSSFeedPlugin, 'read_rss_feed', sizes)
