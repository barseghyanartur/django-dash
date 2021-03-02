from ....contrib.plugins.url.dash_widgets import (
    BaseBookmarkWidget,
    BaseURLWidget,
)

__title__ = 'dash.contrib.layouts.bootstrap2.dash_widgets'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseBookmarkBootstrapTwoWidget',
    'URLBootstrapTwo1x1Bootstrap2FluidMainWidget',
    'URLBootstrapTwo2x2Bootstrap2FluidMainWidget',
)

# *************************************************************
# ******************* URL widgets *****************************
# *************************************************************


class URLBootstrapTwo1x1Bootstrap2FluidMainWidget(BaseURLWidget):
    """URL plugin 1x1 widget for Bootstrap 2 Fluid layout.

    Placeholder `main` widget.
    """

    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'url_bootstrap_two_1x1'
    media_css = (
        'css/dash_plugin_url_bootstrap2.css',
    )


class URLBootstrapTwo2x2Bootstrap2FluidMainWidget(
    URLBootstrapTwo1x1Bootstrap2FluidMainWidget
):
    """URL2x2 plugin widget for Bootstrap 2 Fluid layout.

    Placeholder `main` widget.
    """

    plugin_uid = 'url_bootstrap_two_2x2'
    cols = 2
    rows = 2

# *********************************************************
# *********************************************************
# *********************** Bookmark widgets ****************
# *********************************************************
# *********************************************************


class BaseBookmarkBootstrapTwoWidget(BaseBookmarkWidget):
    """Base Bookmark plugin widget for Bootstrap 2 Fluid layout."""

    media_css = (
        'css/dash_plugin_bookmark_bootstrap2.css',
    )
