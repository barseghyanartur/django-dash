__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Dummy1x1Plugin', 'Dummy1x2Plugin', 'Dummy2x1Plugin', 'Dummy2x2Plugin', 'Dummy3x3Plugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.dummy.forms import DummyForm, DummyShortcutsForm

from dash.contrib.plugins.dummy.dash_widgets import Dummy1x1AndroidMainWidget, Dummy1x1AndroidShortcutWidget
from dash.contrib.plugins.dummy.dash_widgets import Dummy1x1Windows8MainWidget, Dummy1x1Windows8SidebarWidget
from dash.contrib.plugins.dummy.dash_widgets import Dummy2x1AndroidMainWidget, Dummy1x2AndroidMainWidget
from dash.contrib.plugins.dummy.dash_widgets import Dummy1x2AndroidShortcutWidget
from dash.contrib.plugins.dummy.dash_widgets import Dummy3x3AndroidMainWidget

# ***************************************************************************
# ******************************* Dummy plugin ******************************
# ***************************************************************************

class Dummy1x1Plugin(BaseDashboardPlugin):
    """
    Dummy1x1 dashboard plugin.
    """
    uid = 'dummy_1x1'
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


plugin_registry.register(Dummy1x1Plugin)

# ********************************************************************************
# ******************************* Large dummy plugin *****************************
# ********************************************************************************

class Dummy2x1Plugin(Dummy1x1Plugin):
    """
    (Large) dummy2x1 dashboard plugin.
    """
    uid = 'dummy_2x1'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy2x1Plugin)

# ****************************************************************************************
# ******************************* Large dummy portrait plugin ****************************
# ****************************************************************************************

class Dummy1x2Plugin(Dummy1x1Plugin):
    """
    (Large) dummy1x2 (portrait) dashboard plugin.
    """
    uid = 'dummy_1x2'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy1x2Plugin)

# ********************************************************************************
# ******************************* Big dummy plugin *******************************
# ********************************************************************************

class Dummy2x2Plugin(Dummy1x1Plugin):
    """
    Dummy2x2 dashboard plugin.
    """
    uid = 'dummy_2x2'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy2x2Plugin)

# ********************************************************************************
# ******************************* Dummy 3x3 plugin *******************************
# ********************************************************************************

class Dummy3x3Plugin(Dummy1x1Plugin):
    """
    (Big) dummy3x3 dashboard plugin.
    """
    uid = 'dummy_3x3'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy3x3Plugin)


# ********************************************************************************
# ******************************* Dummy 4x4 plugin *******************************
# ********************************************************************************

class Dummy4x4Plugin(Dummy1x1Plugin):
    """
    Dummy4x4 dashboard plugin.
    """
    uid = 'dummy_4x4'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy4x4Plugin)

# ********************************************************************************
# ******************************* Dummy 5x5 plugin *******************************
# ********************************************************************************

class Dummy5x5Plugin(Dummy1x1Plugin):
    """
    Dummy5x5 dashboard plugin.
    """
    uid = 'dummy_5x5'
    name = _("Dummy")
    group = _("Dummy")


plugin_registry.register(Dummy5x5Plugin)

# ********************************************************************************
# ******************************* Registering the widgets ************************
# ********************************************************************************

# Registering the Android widgets for Dummy plugin.
plugin_widget_registry.register(Dummy1x1AndroidMainWidget)
plugin_widget_registry.register(Dummy1x1AndroidShortcutWidget)

# Registering the Windows8 widgets for Dummy plugin.
plugin_widget_registry.register(Dummy1x1Windows8MainWidget)
plugin_widget_registry.register(Dummy1x1Windows8SidebarWidget)

# Registering the Android widgets for Large dummy plugin.
plugin_widget_registry.register(Dummy2x1AndroidMainWidget)

# Registering the Android widgets for LargeDummy plugin.
plugin_widget_registry.register(Dummy1x2AndroidMainWidget)
plugin_widget_registry.register(Dummy1x2AndroidShortcutWidget)

# Registering the Android widgets for Big dummy plugin.
plugin_widget_registry.register(Dummy3x3AndroidMainWidget)
