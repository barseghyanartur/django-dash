from django.utils.translation import ugettext_lazy as _

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory
from .forms import MemoForm, TinyMCEMemoForm

__title__ = 'dash.contrib.plugins.memo.dash_plugins'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseMemoPlugin', 'BaseTinyMCEMemoPlugin',)

# ****************************************************************************
# ******************************* Base memo plugin ***************************
# ****************************************************************************


class BaseMemoPlugin(BaseDashboardPlugin):
    """Base memo plugin."""

    name = _("Memo")
    group = _("Memo")
    form = MemoForm


# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************

sizes = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6)
)

plugin_factory(BaseMemoPlugin, 'memo', sizes)

# ****************************************************************************
# ******************************* Base TinyMCE memo plugin *******************
# ****************************************************************************


class BaseTinyMCEMemoPlugin(BaseDashboardPlugin):
    """Memo dashboard plugin."""

    name = _("TinyMCE memo")
    group = _("Memo")
    form = TinyMCEMemoForm
    help_text = _("TinyMCE tags are available here.")


# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************

sizes = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6)
)

plugin_factory(BaseTinyMCEMemoPlugin, 'tinymce_memo', sizes)
