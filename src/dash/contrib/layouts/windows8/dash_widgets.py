__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URL1x1Windows8MainWidget', 'URL1x1Windows8SidebarWidget')

from dash.contrib.plugins.url.dash_widgets import URL1x1Widget

# *********************************************************
# *********************************************************
# *********************** URL widgets *********************
# *********************************************************
# *********************************************************

class URL1x1Windows8MainWidget(URL1x1Widget):
    """
    URL plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'

    media_css = (
        'css/dash_plugin_url_windows8.css',
    )


class URL1x1Windows8SidebarWidget(URL1x1Windows8MainWidget):
    """
    URL plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
