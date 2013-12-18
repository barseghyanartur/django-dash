__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URL1x1AndroidMainWidget', 'URL1x1AndroidShortcutWidget', 'BaseBookmarkAndroidWidget')

from dash.contrib.plugins.url.dash_widgets import URL1x1Widget, BaseBookmarkWidget

# *********************************************************
# *********************************************************
# *********************** URL widgets *********************
# *********************************************************
# *********************************************************

class URL1x1AndroidMainWidget(URL1x1Widget):
    """
    URL plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'

    media_css = (
        'css/dash_plugin_url_android.css',
    )


class URL1x1AndroidShortcutWidget(URL1x1AndroidMainWidget):
    """
    URL plugin widget for Android layout (placeholder `shortcuts`).
    """
    placeholder_uid = 'shortcuts'


# *********************************************************
# *********************************************************
# *********************** Bookmark widgets ****************
# *********************************************************
# *********************************************************

class BaseBookmarkAndroidWidget(BaseBookmarkWidget):
    """
    Base Bookmark plugin widget for Android layout.
    """
    media_css = (
        'css/dash_plugin_bookmark_android.css',
    )
