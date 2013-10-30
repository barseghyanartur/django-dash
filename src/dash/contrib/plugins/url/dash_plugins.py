__all__ = ('URLPlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.url.forms import URLForm
from dash.contrib.plugins.url.dash_widgets import URLAndroidMainWidget, URLAndroidShortcutWidget
from dash.contrib.plugins.url.dash_widgets import URLWindows8MainWidget, URLWindows8SidebarWidget

# *************************************************************************
# ******************************* URL plugin ******************************
# *************************************************************************

class URLPlugin(BaseDashboardPlugin):
    """
    URL dashboard plugin.
    """
    uid = 'url'
    name = _("URL")
    group = _("URLs")
    form = URLForm

    @property
    def html_class(self):
        """
        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(URLPlugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

plugin_registry.register(URLPlugin)

# *************************************************************************
# ****************** Registering the widgets for URL plugin ***************
# *************************************************************************

# Registering the Android widgets for URL plugin.
plugin_widget_registry.register(URLAndroidMainWidget)
plugin_widget_registry.register(URLAndroidShortcutWidget)

# Registering the Windows8widgets for URL plugin.
plugin_widget_registry.register(URLWindows8MainWidget)
plugin_widget_registry.register(URLWindows8SidebarWidget)
