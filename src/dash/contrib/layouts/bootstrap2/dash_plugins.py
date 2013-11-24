__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from dash.base import plugin_registry, plugin_widget_registry

from dash.contrib.plugins.url.dash_plugins import URL1x1Plugin
from dash.contrib.layouts.bootstrap2.dash_widgets import (
    Dummy1x1Bootstrap2FluidMainWidget, Dummy2x2Bootstrap2FluidMainWidget,
    Image1x1Bootstrap2FluidMainWidget, Image2x2Bootstrap2FluidMainWidget,
    Image3x2Bootstrap2FluidMainWidget, Image3x3Bootstrap2FluidMainWidget,
    Image3x4Bootstrap2FluidMainWidget, Image4x4Bootstrap2FluidMainWidget,
    Image4x5Bootstrap2FluidMainWidget, Image5x4Bootstrap2FluidMainWidget,
    Image5x5Bootstrap2FluidMainWidget,
    Memo2x2Bootstrap2FluidMainWidget, Memo3x3Bootstrap2FluidMainWidget,
    Memo4x5Bootstrap2FluidMainWidget, Memo5x5Bootstrap2FluidMainWidget,
    TinyMCE2x2Bootstrap2FluidMainWidget, TinyMCE3x3Bootstrap2FluidMainWidget,
    TinyMCE4x4Bootstrap2FluidMainWidget, TinyMCE5x5Bootstrap2FluidMainWidget,
    URLBootstrapTwo1x1Bootstrap2FluidMainWidget, URLBootstrapTwo2x2Bootstrap2FluidMainWidget,
    Video2x2Bootstrap2FluidMainWidget, Video3x3Bootstrap2FluidMainWidget,
    Video4x4Bootstrap2FluidMainWidget, Video5x5Bootstrap2FluidMainWidget,
    )
from dash.contrib.layouts.bootstrap2.forms import URLBootstrapTwoForm

# ******************************************************
# ******************* Custom plugins *******************
# ******************************************************

class URLBootstrapTwo1x1Plugin(URL1x1Plugin):
    """
    URL dashboard plugin. The original `URLPlugin`, as well as the main dash.css, relies on presence of
    wonderful "Font awesome". Although a lot of icon names are common between Bootstrap 2 and Font awesome,
    there are some specific icons, that are not present in both. Thus, the original `URLPlugin` is
    extended to address those differences.
    """
    uid = 'url_bootstrap_two_1x1'
    form = URLBootstrapTwoForm


plugin_registry.register(URLBootstrapTwo1x1Plugin)


class URLBootstrapTwo2x2Plugin(URLBootstrapTwo1x1Plugin):
    """
    URL dashboard plugin.
    """
    uid = 'url_bootstrap_two_2x2'


plugin_registry.register(URLBootstrapTwo2x2Plugin)

# ******************************************************
# ***************** Registering widgets ****************
# ******************************************************

# Registering dummy plugin widgets
plugin_widget_registry.register(Dummy1x1Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Dummy2x2Bootstrap2FluidMainWidget)

# Registering image plugin widgets
plugin_widget_registry.register(Image1x1Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image2x2Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image3x2Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image3x3Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image3x4Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image4x4Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image4x5Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image5x4Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Image5x5Bootstrap2FluidMainWidget)

# Registering memo plugin widgets
plugin_widget_registry.register(Memo2x2Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Memo3x3Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Memo4x5Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Memo5x5Bootstrap2FluidMainWidget)
plugin_widget_registry.register(TinyMCE2x2Bootstrap2FluidMainWidget)
plugin_widget_registry.register(TinyMCE3x3Bootstrap2FluidMainWidget)
plugin_widget_registry.register(TinyMCE4x4Bootstrap2FluidMainWidget)
plugin_widget_registry.register(TinyMCE5x5Bootstrap2FluidMainWidget)

# Registering URL plugin widgets
plugin_widget_registry.register(URLBootstrapTwo1x1Bootstrap2FluidMainWidget)
#plugin_widget_registry.register(URLBootstrapTwo2x2Bootstrap2FluidMainWidget)

# Registering Video plugin widgets
plugin_widget_registry.register(Video2x2Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Video3x3Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Video4x4Bootstrap2FluidMainWidget)
plugin_widget_registry.register(Video5x5Bootstrap2FluidMainWidget)
