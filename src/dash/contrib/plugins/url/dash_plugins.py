__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URL1x1Plugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.url.forms import URLForm
from dash.contrib.plugins.url.dash_widgets import URL1x1AndroidMainWidget, URL1x1AndroidShortcutWidget
from dash.contrib.plugins.url.dash_widgets import URL1x1Windows8MainWidget, URL1x1Windows8SidebarWidget

# *************************************************************************
# ******************************* URL plugin ******************************
# *************************************************************************

class URL1x1Plugin(BaseDashboardPlugin):
    """
    URL dashboard plugin.
    """
    uid = 'url_1x1'
    name = _("URL")
    group = _("URLs")
    form = URLForm

    @property
    def html_class(self):
        """
        If plugin has an image, we add a class `iconic` to it.
        """
        html_class = super(URL1x1Plugin, self).html_class
        if self.data.image:
            html_class += ' iconic-url'
        return html_class

plugin_registry.register(URL1x1Plugin)

# *************************************************************************
# ****************** Registering the widgets for URL plugin ***************
# *************************************************************************

# Registering the Android widgets for URL plugin.
plugin_widget_registry.register(URL1x1AndroidMainWidget)
plugin_widget_registry.register(URL1x1AndroidShortcutWidget)

# Registering the Windows8widgets for URL plugin.
plugin_widget_registry.register(URL1x1Windows8MainWidget)
plugin_widget_registry.register(URL1x1Windows8SidebarWidget)
