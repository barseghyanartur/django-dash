from ....contrib.plugins.url.dash_widgets import (
    BaseBookmarkWidget,
    URL1x1Widget,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseBookmarkAndroidWidget',
    'URL1x1AndroidMainWidget',
    'URL1x1AndroidShortcutWidget',
)

# *********************************************************
# *********************************************************
# *********************** URL widgets *********************
# *********************************************************
# *********************************************************


class URL1x1AndroidMainWidget(URL1x1Widget):
    """URL plugin widget for Android layout (placeholder `main`)."""

    layout_uid = 'android'
    placeholder_uid = 'main'
    media_css = (
        'css/dash_plugin_url_android.css',
    )


class URL1x1AndroidShortcutWidget(URL1x1AndroidMainWidget):
    """URL plugin widget for Android layout (placeholder `shortcuts`)."""

    placeholder_uid = 'shortcuts'


# *********************************************************
# *********************************************************
# *********************** Bookmark widgets ****************
# *********************************************************
# *********************************************************

class BaseBookmarkAndroidWidget(BaseBookmarkWidget):
    """Base Bookmark plugin widget for Android layout."""

    media_css = (
        'css/dash_plugin_bookmark_android.css',
    )
