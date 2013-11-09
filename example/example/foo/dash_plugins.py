from dash.base import plugin_registry, plugin_widget_registry
from dash.contrib.plugins.image.dash_plugins import Image1x1Plugin

from foo.dash_widgets import (
    Dummy1x1ExampleMainWidget, Dummy2x2ExampleMainWidget,
    Dummy1x1ExampleTopShortcutsWidget,
    Dummy1x1ExampleRightShortcutsWidget, Dummy2x2ExampleRightShortcutsWidget,
    Dummy1x1ExampleBottomShortcutsWidget,
    Dummy1x1ExampleLeftShortcutsWidget, Dummy2x2ExampleLeftShortcutsWidget,
    Image1x1ExampleMainWidget, Image2x2ExampleMainWidget, Image3x2ExampleMainWidget, Image3x3ExampleMainWidget,
    Image3x8ExampleLeftShortcutsWidget, Image3x8ExampleRightShortcutsWidget,
    Image8x1ExampleTopShortcutsWidget, Image8x1ExampleBottomShortcutsWidget,
    Memo2x2ExampleMainWidget, Memo3x3ExampleMainWidget,
    TinyMCE2x2ExampleMainWidget, TinyMCE3x3ExampleMainWidget,
    URL1x1ExampleMainWidget, URL2x2ExampleMainWidget,
    Video2x2ExampleMainWidget, Video3x3ExampleMainWidget,
    )

# ******************************************************
# ******************Extended plugins *******************
# ******************************************************

class Image3x8Plugin(Image1x1Plugin):
    """
    Image3x8 dashboard plugin.
    """
    uid = 'image_3x8'


plugin_registry.register(Image3x8Plugin)


class Image8x1Plugin(Image1x1Plugin):
    """
    Image3x8 dashboard plugin.
    """
    uid = 'image_8x1'


plugin_registry.register(Image8x1Plugin)

# ******************************************************
# ***************** Registering widgets ****************
# ******************************************************

# Registering dummy plugin widgets
plugin_widget_registry.register(Dummy1x1ExampleMainWidget)
plugin_widget_registry.register(Dummy2x2ExampleMainWidget)

plugin_widget_registry.register(Dummy1x1ExampleTopShortcutsWidget)

plugin_widget_registry.register(Dummy1x1ExampleRightShortcutsWidget)
plugin_widget_registry.register(Dummy2x2ExampleRightShortcutsWidget)

plugin_widget_registry.register(Dummy1x1ExampleBottomShortcutsWidget)

plugin_widget_registry.register(Dummy1x1ExampleLeftShortcutsWidget)
plugin_widget_registry.register(Dummy2x2ExampleLeftShortcutsWidget)

# Registering image plugin widgets
plugin_widget_registry.register(Image1x1ExampleMainWidget)
plugin_widget_registry.register(Image2x2ExampleMainWidget)
plugin_widget_registry.register(Image3x2ExampleMainWidget)
plugin_widget_registry.register(Image3x3ExampleMainWidget)

plugin_widget_registry.register(Image3x8ExampleLeftShortcutsWidget)
plugin_widget_registry.register(Image3x8ExampleRightShortcutsWidget)
plugin_widget_registry.register(Image8x1ExampleTopShortcutsWidget)
plugin_widget_registry.register(Image8x1ExampleBottomShortcutsWidget)

# Registering memo plugin widgets
plugin_widget_registry.register(Memo2x2ExampleMainWidget)
plugin_widget_registry.register(Memo3x3ExampleMainWidget)
plugin_widget_registry.register(TinyMCE2x2ExampleMainWidget)
plugin_widget_registry.register(TinyMCE3x3ExampleMainWidget)

# Registering URL plugin widgets
plugin_widget_registry.register(URL1x1ExampleMainWidget)
plugin_widget_registry.register(URL2x2ExampleMainWidget)

# Registering Video plugin widgets
plugin_widget_registry.register(Video2x2ExampleMainWidget)
plugin_widget_registry.register(Video3x3ExampleMainWidget)
