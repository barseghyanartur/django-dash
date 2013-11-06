__all__ = ('ImagePlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.image.forms import ImageForm
from dash.contrib.plugins.image.dash_widgets import ImageAndroidMainWidget
from dash.contrib.plugins.image.dash_widgets import ImageWindows8MainWidget, ImageWindows8SidebarWidget

# *************************************************************************
# ******************************* Image plugin ****************************
# *************************************************************************

class ImagePlugin(BaseDashboardPlugin):
    """
    Image dashboard plugin.
    """
    uid = 'image'
    name = _("Image")
    group = _("Image")
    form = ImageForm


plugin_registry.register(ImagePlugin)

# *************************************************************************
# ****************** Registering the widgets for Image plugin *************
# *************************************************************************

# Registering the Android widgets for Image plugin.
plugin_widget_registry.register(ImageAndroidMainWidget)

# Registering the Windows8widgets for Image plugin.
plugin_widget_registry.register(ImageWindows8MainWidget)
plugin_widget_registry.register(ImageWindows8SidebarWidget)
