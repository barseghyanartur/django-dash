from ....base import plugin_widget_registry
from ....factory import plugin_widget_factory

from ....contrib.plugins.dummy.dash_widgets import BaseDummyWidget
from ....contrib.plugins.image.dash_widgets import BaseImageWidget
from ....contrib.plugins.memo.dash_widgets import BaseMemoWidget
from ....contrib.plugins.rss_feed.dash_widgets import BaseReadRSSFeedWidget
from ....contrib.plugins.video.dash_widgets import BaseVideoWidget
from ....contrib.layouts.windows8.dash_widgets import (
    BaseBookmarkWindows8Widget,
    URL1x1Windows8MainWidget,
    URL1x1Windows8SidebarWidget,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'

# **************************************************************************
# **************************************************************************
# **************************************************************************
# ************************* Registering the widgets ************************
# **************************************************************************
# **************************************************************************
# **************************************************************************

# **************************************************************************
# ******************* Registering widgets for Dummy plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
)
sidebar_sizes = (
    (1, 1),
)
plugin_widget_factory(BaseDummyWidget,
                      'windows8',
                      'main',
                      'dummy',
                      main_sizes)
plugin_widget_factory(BaseDummyWidget,
                      'windows8',
                      'sidebar',
                      'dummy',
                      sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for Image plugin *****************
# **************************************************************************


main_sizes = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)
sidebar_sizes = (
    (1, 1),
    (2, 2),
)
plugin_widget_factory(BaseImageWidget,
                      'windows8',
                      'main',
                      'image',
                      main_sizes)
plugin_widget_factory(BaseImageWidget,
                      'windows8',
                      'sidebar',
                      'image',
                      sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for Memo plugin ******************
# **************************************************************************


main_sizes = (
    (2, 2),
    (3, 3),
)
sidebar_sizes = (
    (2, 2),
)
plugin_widget_factory(BaseMemoWidget,
                      'windows8',
                      'main',
                      'memo',
                      main_sizes)
plugin_widget_factory(BaseMemoWidget,
                      'windows8',
                      'sidebar',
                      'memo',
                      sidebar_sizes)

# **************************************************************************
# ******************* Registering widgets for RSS plugin *******************
# **************************************************************************


main_sizes = (
    (2, 3),
)
sidebar_sizes = (
    (2, 3),
)
plugin_widget_factory(BaseReadRSSFeedWidget,
                      'windows8',
                      'main',
                      'read_rss_feed',
                      main_sizes)
plugin_widget_factory(BaseReadRSSFeedWidget,
                      'windows8',
                      'sidebar',
                      'read_rss_feed',
                      sidebar_sizes)

# **************************************************************************
# ******************* Registering the widgets for URL plugin ***************
# **************************************************************************


plugin_widget_registry.register(URL1x1Windows8MainWidget)
plugin_widget_registry.register(URL1x1Windows8SidebarWidget)

# **************************************************************************
# ***************** Registering the widgets for Video plugin ***************
# **************************************************************************


main_sizes = (
    (2, 2),
)
sidebar_sizes = (
    (2, 3),
)
plugin_widget_factory(BaseVideoWidget,
                      'windows8',
                      'main',
                      'video',
                      main_sizes)
plugin_widget_factory(BaseVideoWidget,
                      'windows8',
                      'sidebar',
                      'video',
                      sidebar_sizes)

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
plugin_widget_factory(BaseBookmarkWindows8Widget,
                      'windows8',
                      'main',
                      'bookmark',
                      main_sizes)
plugin_widget_factory(BaseBookmarkWindows8Widget,
                      'windows8',
                      'sidebar',
                      'bookmark',
                      shortcut_sizes)
