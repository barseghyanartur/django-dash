__all__ = ('Memo1x1Plugin', 'Memo2x2Plugin', 'Memo3x3Plugin', 'Memo4x5Plugin', 'TinyMCEMemo2x2Plugin',
           'TinyMCEMemo3x3Plugin')

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.memo.forms import MemoForm, TinyMCEMemoForm
from dash.contrib.plugins.memo.dash_widgets import Memo2x2AndroidMainWidget, Memo1x1AndroidShortcutWidget
from dash.contrib.plugins.memo.dash_widgets import Memo3x3AndroidMainWidget, Memo3x3Windows8MainWidget
from dash.contrib.plugins.memo.dash_widgets import Memo4x5AndroidMainWidget, TinyMCEMemo2x2AndroidMainWidget
from dash.contrib.plugins.memo.dash_widgets import TinyMCEMemo3x3AndroidMainWidget, Memo2x2Windows8MainWidget
from dash.contrib.plugins.memo.dash_widgets import Memo2x2Windows8SidebarWidget

# **************************************************************************
# ******************************* MemoPlugin *******************************
# **************************************************************************

class Memo2x2Plugin(BaseDashboardPlugin):
    """
    Memo dashboard plugin.
    """
    uid = 'memo_2x2'
    name = _("Memo")
    group = _("Memo")
    form = MemoForm


plugin_registry.register(Memo2x2Plugin)

# **************************************************************************
# ******************************* Memo1x1 Plugin ***************************
# **************************************************************************

class Memo1x1Plugin(Memo2x2Plugin):
    """
    Memo1x1 dashboard plugin.
    """
    uid = 'memo_1x1'

plugin_registry.register(Memo1x1Plugin)

# **************************************************************************
# ******************************* Big memo plugin **************************
# **************************************************************************

class Memo3x3Plugin(Memo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'memo_3x3'

plugin_registry.register(Memo3x3Plugin)

# **************************************************************************
# ******************************* 4x5 memo plugin *************************
# **************************************************************************

class Memo4x5Plugin(Memo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'memo_4x5'

plugin_registry.register(Memo4x5Plugin)


# **************************************************************************
# ******************************* Memo 5x5 plugin **************************
# **************************************************************************

class Memo5x5Plugin(Memo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'memo_5x5'

plugin_registry.register(Memo5x5Plugin)

# **************************************************************************
# ******************************* Memo 6x6 plugin **************************
# **************************************************************************

class Memo6x6Plugin(Memo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'memo_6x6'

plugin_registry.register(Memo6x6Plugin)

# **************************************************************************
# ******************************* TinyMCE memo 2x2 plugin ******************
# **************************************************************************

class TinyMCEMemo2x2Plugin(BaseDashboardPlugin):
    """
    Memo dashboard plugin.
    """
    uid = 'tinymce_memo_2x2'
    name = _("TinyMCE memo")
    group = _("Memo")
    form = TinyMCEMemoForm
    help_text = _("""TinyMCE tags are available here.""")


plugin_registry.register(TinyMCEMemo2x2Plugin)

# **************************************************************************
# ******************************* TinyMCE memo 3x3 plugin ******************
# **************************************************************************

class TinyMCEMemo3x3Plugin(TinyMCEMemo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'tinymce_memo_3x3'

plugin_registry.register(TinyMCEMemo3x3Plugin)

# **************************************************************************
# ******************************* TinyMCE memo 4x4 plugin ******************
# **************************************************************************

class TinyMCEMemo4x4Plugin(TinyMCEMemo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'tinymce_memo_4x4'

plugin_registry.register(TinyMCEMemo4x4Plugin)

# **************************************************************************
# ******************************* TinyMCE memo 5x5 plugin ******************
# **************************************************************************

class TinyMCEMemo5x5Plugin(TinyMCEMemo2x2Plugin):
    """
    Exact copy of the memo plugin, just rendered bigger.
    """
    uid = 'tinymce_memo_5x5'

plugin_registry.register(TinyMCEMemo5x5Plugin)

# **************************************************************************
# ****************** Registering the widgets *******************************
# **************************************************************************

# Registering the Android widgets for Memo plugin.
plugin_widget_registry.register(Memo2x2AndroidMainWidget)
plugin_widget_registry.register(Memo1x1AndroidShortcutWidget)

# Registering the Android widgets for Big memo plugin.
plugin_widget_registry.register(Memo3x3AndroidMainWidget)

# Registering the Windows8 widgets for Big memo plugin.
plugin_widget_registry.register(Memo3x3Windows8MainWidget)

# Registering the Android widgets for Huge memo plugin.
plugin_widget_registry.register(Memo4x5AndroidMainWidget)

# Registering the Android widgets for TinyMCE memo plugin.
plugin_widget_registry.register(TinyMCEMemo2x2AndroidMainWidget)

# Registering the Android widgets for Big TinyMCE memo plugin.
plugin_widget_registry.register(TinyMCEMemo3x3AndroidMainWidget)

# Registering the Windows 8 widgets for Memo plugin.
plugin_widget_registry.register(Memo2x2Windows8MainWidget)
plugin_widget_registry.register(Memo2x2Windows8SidebarWidget)
