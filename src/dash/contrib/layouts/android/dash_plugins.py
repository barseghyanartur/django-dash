from ....base import plugin_widget_registry
from ....factory import plugin_widget_factory
from ....contrib.plugins.dummy.dash_widgets import BaseDummyWidget
from ....contrib.plugins.image.dash_widgets import BaseImageWidget
from ....contrib.plugins.memo.dash_widgets import (
    BaseMemoWidget,
    BaseTinyMCEMemoWidget,
)
from ....contrib.plugins.rss_feed.dash_widgets import BaseReadRSSFeedWidget
from ....contrib.plugins.video.dash_widgets import BaseVideoWidget
from ....contrib.plugins.weather.dash_widgets import BaseWeatherWidget

from .dash_widgets import (
    BaseBookmarkAndroidWidget,
    URL1x1AndroidMainWidget,
    URL1x1AndroidShortcutWidget,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'

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
    (1, 2),
    (2, 1),
    (3, 3),
)
shortcut_sizes = (
    (1, 1),
    (1, 2),
)
plugin_widget_factory(BaseDummyWidget,
                      'android',
                      'main',
                      'dummy',
                      main_sizes)
plugin_widget_factory(BaseDummyWidget,
                      'android',
                      'shortcut',
                      'dummy',
                      shortcut_sizes)

# **************************************************************************
# ******************* Registering widgets for Image plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
)
plugin_widget_factory(BaseImageWidget,
                      'android',
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
)
shortcut_sizes = (
    (1, 1),
)
plugin_widget_factory(BaseMemoWidget,
                      'android',
                      'main',
                      'memo',
                      main_sizes)
plugin_widget_factory(BaseMemoWidget,
                      'android',
                      'shortcut',
                      'memo',
                      shortcut_sizes)

# **************************************************************************
# ************** Registering widgets for TinyMCEMemo plugin ****************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
)
plugin_widget_factory(BaseTinyMCEMemoWidget,
                      'android',
                      'main',
                      'tinymce_memo',
                      main_sizes)

# **************************************************************************
# ******************* Registering widgets for RSS plugin *******************
# **************************************************************************


main_sizes = (
    (2, 3),
    (3, 3),
)
plugin_widget_factory(BaseReadRSSFeedWidget,
                      'android',
                      'main',
                      'read_rss_feed',
                      main_sizes)

# **************************************************************************
# ******************* Registering the widgets for URL plugin ***************
# **************************************************************************


plugin_widget_registry.register(URL1x1AndroidMainWidget)
plugin_widget_registry.register(URL1x1AndroidShortcutWidget)

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
                      'android',
                      'main',
                      'video',
                      main_sizes)

# **************************************************************************
# *************** Registering the widgets for Weather plugin ***************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
)
plugin_widget_factory(BaseWeatherWidget,
                      'android',
                      'main',
                      'weather',
                      main_sizes)

# **************************************************************************
# *************** Registering the widgets for Bookmark plugin ***************
# **************************************************************************


main_sizes = (
    (1, 1),
    # (2, 2),
)
shortcut_sizes = (
    (1, 1),
    # (2, 2),
)
plugin_widget_factory(BaseBookmarkAndroidWidget,
                      'android',
                      'main',
                      'bookmark',
                      main_sizes)
plugin_widget_factory(BaseBookmarkAndroidWidget,
                      'android',
                      'shortcut',
                      'bookmark',
                      shortcut_sizes)
