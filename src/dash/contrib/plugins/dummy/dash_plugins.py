__all__ = ('DummyPlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.dummy.forms import DummyForm, DummyShortcutsForm

from dash.contrib.plugins.dummy.dash_widgets import DummyAndroidMainWidget, DummyAndroidShortcutWidget
from dash.contrib.plugins.dummy.dash_widgets import DummyWindows8MainWidget, DummyWindows8SidebarWidget
from dash.contrib.plugins.dummy.dash_widgets import LargeDummyAndroidMainWidget, LargeDummyPortraitAndroidMainWidget
from dash.contrib.plugins.dummy.dash_widgets import LargeDummyPortraitAndroidShortcutWidget
from dash.contrib.plugins.dummy.dash_widgets import BigDummyAndroidMainWidget

# ***************************************************************************
# ******************************* Dummy plugin ******************************
# ***************************************************************************

class DummyPlugin(BaseDashboardPlugin):
    """
    Dummy dashboard plugin.
    """
    uid = 'dummy'
    name = _("Dummy")
    form = DummyForm
    group = _("Dummy")

    def get_form(self):
        if 'sidebar' == self.placeholder:
            return DummyShortcutsForm
        else:
            return DummyForm

    def post_processor(self):
        """
        If no text available, use dummy.
        """
        if not self.data.text:
            self.data.text = 'Dummy content'


plugin_registry.register(DummyPlugin)

# ********************************************************************************
# ******************************* Large dummy plugin *****************************
# ********************************************************************************

class LargeDummyPlugin(DummyPlugin):
    """
    Large dummy dashboard plugin.
    """
    uid = 'large_dummy'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(LargeDummyPlugin)

# ****************************************************************************************
# ******************************* Large dummy portrait plugin ****************************
# ****************************************************************************************

class LargeDummyPortraitPlugin(DummyPlugin):
    """
    Large dummy portrait dashboard plugin.
    """
    uid = 'large_dummy_portrait'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(LargeDummyPortraitPlugin)

# ********************************************************************************
# ******************************* Big dummy plugin *******************************
# ********************************************************************************

class BigDummyPlugin(DummyPlugin):
    """
    Big dummy dashboard plugin.
    """
    uid = 'big_dummy'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(BigDummyPlugin)

# ********************************************************************************
# ******************************* Registering the widgets ************************
# ********************************************************************************

# Registering the Android widgets for Dummy plugin.
plugin_widget_registry.register(DummyAndroidMainWidget)
plugin_widget_registry.register(DummyAndroidShortcutWidget)

# Registering the Windows8 widgets for Dummy plugin.
plugin_widget_registry.register(DummyWindows8MainWidget)
plugin_widget_registry.register(DummyWindows8SidebarWidget)

# Registering the Android widgets for Large dummy plugin.
plugin_widget_registry.register(LargeDummyAndroidMainWidget)

# Registering the Android widgets for LargeDummy plugin.
plugin_widget_registry.register(LargeDummyPortraitAndroidMainWidget)
plugin_widget_registry.register(LargeDummyPortraitAndroidShortcutWidget)

# Registering the Android widgets for Big dummy plugin.
plugin_widget_registry.register(BigDummyAndroidMainWidget)
