__all__ = ('MemoPlugin', 'BigMemoPlugin', 'HugeMemoPlugin', 'TinyMCEMemoPlugin', \
           'BigTinyMCEMemoPlugin')

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.memo.forms import MemoForm, TinyMCEMemoForm
from dash.contrib.plugins.memo.dash_widgets import MemoAndroidMainWidget, MemoAndroidShortcutWidget
from dash.contrib.plugins.memo.dash_widgets import BigMemoAndroidMainWidget, BigMemoWindows8MainWidget
from dash.contrib.plugins.memo.dash_widgets import HugeMemoAndroidMainWidget, TinyMCEMemoAndroidMainWidget
from dash.contrib.plugins.memo.dash_widgets import BigTinyMCEMemoAndroidMainWidget, MemoWindows8MainWidget
from dash.contrib.plugins.memo.dash_widgets import MemoWindows8SidebarWidget, BigMemoWindows8MainWidget
from dash.contrib.plugins.memo.dash_widgets import BigMemoWindows8SidebarWidget

# **************************************************************************
# ******************************* MemoPlugin *******************************
# **************************************************************************

class MemoPlugin(BaseDashboardPlugin):
    """
    Memo dashboard plugin.
    """
    uid = 'memo'
    name = _("Memo")
    group = _("Memo")
    form = MemoForm


plugin_registry.register(MemoPlugin)

# **************************************************************************
# ******************************* Big memo plugin **************************
# **************************************************************************

class BigMemoPlugin(MemoPlugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'big_memo'
    name = _("Memo")
    group = _("Memo")


plugin_registry.register(BigMemoPlugin)

# **************************************************************************
# ******************************* Huge memo plugin *************************
# **************************************************************************

class HugeMemoPlugin(MemoPlugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'huge_memo'
    name = _("Memo")
    group = _("Memo")


plugin_registry.register(HugeMemoPlugin)


# **************************************************************************
# ******************************* TinyMCE memo plugin **********************
# **************************************************************************

class TinyMCEMemoPlugin(BaseDashboardPlugin):
    """
    Memo dashboard plugin.
    """
    uid = 'tinymce_memo'
    name = _("TinyMCE memo")
    group = _("Memo")
    form = TinyMCEMemoForm
    help_text = _("""TinyMCE tags are available here.""")


plugin_registry.register(TinyMCEMemoPlugin)

# **************************************************************************
# ******************************* Big TinyMCE memo plugin ******************
# **************************************************************************

class BigTinyMCEMemoPlugin(TinyMCEMemoPlugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'big_tinymce_memo'
    name = _("TinyMCE memo")
    group = _("Memo")


plugin_registry.register(BigTinyMCEMemoPlugin)

# **************************************************************************
# ****************** Registering the widgets *******************************
# **************************************************************************

# Registering the Android widgets for Memo plugin.
plugin_widget_registry.register(MemoAndroidMainWidget)
plugin_widget_registry.register(MemoAndroidShortcutWidget)

# Registering the Android widgets for Big memo plugin.
plugin_widget_registry.register(BigMemoAndroidMainWidget)

# Registering the Windows8 widgets for Big memo plugin.
plugin_widget_registry.register(BigMemoWindows8MainWidget)

# Registering the Android widgets for Huge memo plugin.
plugin_widget_registry.register(HugeMemoAndroidMainWidget)

# Registering the Android widgets for TinyMCE memo plugin.
plugin_widget_registry.register(TinyMCEMemoAndroidMainWidget)

# Registering the Android widgets for Big TinyMCE memo plugin.
plugin_widget_registry.register(BigTinyMCEMemoAndroidMainWidget)

# Registering the Windows 8 widgets for Memo plugin.
plugin_widget_registry.register(MemoWindows8MainWidget)
plugin_widget_registry.register(MemoWindows8SidebarWidget)

# Registering the Windows 8 widgets for BigMemo plugin.
plugin_widget_registry.register(BigMemoWindows8MainWidget)
plugin_widget_registry.register(BigMemoWindows8SidebarWidget)
