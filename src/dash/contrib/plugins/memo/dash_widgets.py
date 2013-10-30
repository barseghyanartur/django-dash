__all__ = ('MemoAndroidMainWidget', 'MemoAndroidShortcutWidget', 'BigMemoAndroidMainWidget', \
           'BigMemoWindows8MainWidget', 'HugeMemoAndroidMainWidget', 'TinyMCEMemoAndroidMainWidget', \
           'BigTinyMCEMemoAndroidMainWidget', 'MemoWindows8MainWidget', 'MemoWindows8SidebarWidget', \
           'BigMemoWindows8MainWidget', 'BigMemoWindows8SidebarWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ***********************************************************************
# ****************** Android widgets for Memo plugin ********************
# ***********************************************************************

class MemoAndroidMainWidget(BaseDashboardPluginWidget):
    """
    Memo plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'memo'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_main.html', context)


class MemoAndroidShortcutWidget(MemoAndroidMainWidget):
    """
    Memo plugin widget for Android layout (placeholder `shortcuts`).
    """
    placeholder_uid = 'shortcuts'
    cols = 1
    rows = 1

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_shortcuts.html', context)

# ***************************************************************************
# ****************** Android widgets for Big memo plugin ********************
# ***************************************************************************

class BigMemoAndroidMainWidget(MemoAndroidMainWidget):
    """
    Big memo plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'big_memo'
    cols = 3
    rows = 3

# ***************************************************************************
# ****************** Windows8 widgets for Big memo plugin *******************
# ***************************************************************************

class BigMemoWindows8MainWidget(BigMemoAndroidMainWidget):
    """
    Big memo plugin widget for Windows8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'

# ***************************************************************************
# ****************** Android widgets for Huge memo plugin *******************
# ***************************************************************************

class HugeMemoAndroidMainWidget(MemoAndroidMainWidget):
    """
    Huge memo plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'huge_memo'
    cols = 4
    rows = 5


# ***********************************************************************
# ****************** Android widgets for TinyMCEMemo plugin *************
# ***********************************************************************

class TinyMCEMemoAndroidMainWidget(BaseDashboardPluginWidget):
    """
    TinyMCE memo plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'tinymce_memo'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('tinymce/render_main.html', context)

# ***************************************************************************
# ****************** Android widgets for Big TinyMCE memo plugin ************
# ***************************************************************************

class BigTinyMCEMemoAndroidMainWidget(TinyMCEMemoAndroidMainWidget):
    """
    Big memo plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'big_tinymce_memo'
    cols = 3
    rows = 3


# ***********************************************************************
# ****************** Windows8 widgets for Memo plugin *******************
# ***********************************************************************

class MemoWindows8MainWidget(BaseDashboardPluginWidget):
    """
    Memo plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'memo'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_main.html', context)


class MemoWindows8SidebarWidget(MemoWindows8MainWidget):
    """
    Memo plugin widget for Windows8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
    cols = 1
    rows = 1

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_shortcuts.html', context)


# ***************************************************************************
# ****************** Windows 8 widgets for Big memo plugin ******************
# ***************************************************************************

class BigMemoWindows8MainWidget(MemoAndroidMainWidget):
    """
    Big memo plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    plugin_uid = 'big_memo'
    cols = 3
    rows = 3


class BigMemoWindows8SidebarWidget(BigMemoWindows8MainWidget):
    """
    Big memo plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'sidebar'
    plugin_uid = 'big_memo'
    cols = 2
    rows = 2

