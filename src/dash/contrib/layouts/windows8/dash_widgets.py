from ....contrib.plugins.url.dash_widgets import (
    BaseBookmarkWidget,
    URL1x1Widget,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseBookmarkWindows8Widget',
    'URL1x1Windows8MainWidget',
    'URL1x1Windows8SidebarWidget',
)


# *********************************************************
# *********************************************************
# *********************** URL widgets *********************
# *********************************************************
# *********************************************************

class URL1x1Windows8MainWidget(URL1x1Widget):
    """URL plugin widget for Windows 8 layout (placeholder `main`)."""

    layout_uid = 'windows8'
    placeholder_uid = 'main'
    media_css = (
        'css/dash_plugin_url_windows8.css',
    )


class URL1x1Windows8SidebarWidget(URL1x1Windows8MainWidget):
    """URL plugin widget for Windows 8 layout (placeholder `sidebar`)."""

    placeholder_uid = 'sidebar'

# *********************************************************
# *********************************************************
# *********************** Bookmark widgets ****************
# *********************************************************
# *********************************************************


class BaseBookmarkWindows8Widget(BaseBookmarkWidget):
    """Base Bookmark plugin widget for Windows8 layout."""

    media_css = (
        'css/dash_plugin_bookmark_windows8.css',
    )
