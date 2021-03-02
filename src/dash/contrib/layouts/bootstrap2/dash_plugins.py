from ....base import plugin_registry, plugin_widget_registry
from ....factory import plugin_widget_factory

from ....contrib.plugins.dummy.dash_widgets import BaseDummyWidget
from ....contrib.plugins.image.dash_widgets import BaseImageWidget
from ....contrib.plugins.memo.dash_widgets import (
    BaseMemoWidget,
    BaseTinyMCEMemoWidget,
)
from ....contrib.plugins.video.dash_widgets import BaseVideoWidget
from ....contrib.plugins.url.dash_plugins import BaseURLPlugin
from .dash_widgets import (
    BaseBookmarkBootstrapTwoWidget,
    URLBootstrapTwo1x1Bootstrap2FluidMainWidget,
)
from .forms import URLBootstrapTwoForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'URLBootstrapTwo1x1Plugin',
    'URLBootstrapTwo2x2Plugin',
)

# **************************************************************************
# ****************************** Custom plugins ****************************
# **************************************************************************


class URLBootstrapTwo1x1Plugin(BaseURLPlugin):
    """URL dashboard plugin.

    The original `URLPlugin`, as well as the main dash.css, relies on
    presence of wonderful "Font awesome". Although a lot of icon names are
    common between Bootstrap 2 and Font awesome, there are some specific
    icons, that are not present in both. Thus, the original ``URLPlugin`` is
    extended to address those differences.
    """

    uid = 'url_bootstrap_two_1x1'
    form = URLBootstrapTwoForm


plugin_registry.register(URLBootstrapTwo1x1Plugin)


class URLBootstrapTwo2x2Plugin(URLBootstrapTwo1x1Plugin):
    """URL dashboard plugin."""

    uid = 'url_bootstrap_two_2x2'


plugin_registry.register(URLBootstrapTwo2x2Plugin)

# **************************************************************************
# **************************************************************************
# ************************** Registering the widgets ***********************
# **************************************************************************
# **************************************************************************

# **************************************************************************
# ******************* Registering widgets for Dummy plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (2, 2),
)
plugin_widget_factory(BaseDummyWidget,
                      'bootstrap2_fluid',
                      'main',
                      'dummy',
                      main_sizes)

# **************************************************************************
# ******************* Registering widgets for Image plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5),
)
plugin_widget_factory(BaseImageWidget,
                      'bootstrap2_fluid',
                      'main',
                      'image',
                      main_sizes)

# **************************************************************************
# ******************* Registering widgets for Memo plugin ******************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 5),
)
plugin_widget_factory(BaseMemoWidget,
                      'bootstrap2_fluid',
                      'main',
                      'memo',
                      main_sizes)

# **************************************************************************
# ************** Registering widgets for TinyMCEMemo plugin ****************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 5),
)
plugin_widget_factory(BaseTinyMCEMemoWidget,
                      'bootstrap2_fluid',
                      'main',
                      'tinymce_memo',
                      main_sizes)

# **************************************************************************
# ******************* Registering the widgets for URL plugin ***************
# **************************************************************************


# Registering URL plugin widgets
plugin_widget_registry.register(URLBootstrapTwo1x1Bootstrap2FluidMainWidget)
# plugin_widget_registry.register(URLBootstrapTwo2x2Bootstrap2FluidMainWidget)

# **************************************************************************
# ***************** Registering the widgets for Video plugin ***************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
plugin_widget_factory(BaseVideoWidget,
                      'bootstrap2_fluid',
                      'main',
                      'video',
                      main_sizes)

# **************************************************************************
# *************** Registering the widgets for Bookmark plugin ***************
# **************************************************************************


main_sizes = (
    (1, 1),
    # (2, 2),
)
plugin_widget_factory(BaseBookmarkBootstrapTwoWidget,
                      'bootstrap2_fluid',
                      'main',
                      'bookmark',
                      main_sizes)
