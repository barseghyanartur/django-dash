__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Memo1x1AndroidShortcutWidget', 'Memo2x2AndroidMainWidget', 'Memo2x2Windows8MainWidget',
           'Memo2x2Windows8SidebarWidget', 'Memo3x3AndroidMainWidget', 'Memo3x3Windows8MainWidget',
           'Memo3x3Windows8MainWidget', 'Memo4x5AndroidMainWidget', 'TinyMCEMemo2x2AndroidMainWidget',
           'TinyMCEMemo3x3AndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ***********************************************************************
# ****************** Android widgets for Memo plugin ********************
# ***********************************************************************

class Memo2x2AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Memo2x2 plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'memo_2x2'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_main.html', context)


class Memo1x1AndroidShortcutWidget(Memo2x2AndroidMainWidget):
    """
    Memo1x1 plugin widget for Android layout (placeholder `shortcuts`).
    """
    placeholder_uid = 'shortcuts'
    plugin_uid = 'memo_1x1'
    cols = 1
    rows = 1

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_shortcuts.html', context)

# ***************************************************************************
# ****************** Android widgets for Big memo plugin ********************
# ***************************************************************************

class Memo3x3AndroidMainWidget(Memo2x2AndroidMainWidget):
    """
    Memo3x3 plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'memo_3x3'
    cols = 3
    rows = 3

# ***************************************************************************
# ****************** Android widgets for Huge memo plugin *******************
# ***************************************************************************

class Memo4x5AndroidMainWidget(Memo2x2AndroidMainWidget):
    """
    Huge memo plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'memo_4x5'
    cols = 4
    rows = 5


# ***********************************************************************
# ****************** Android widgets for TinyMCEMemo plugin *************
# ***********************************************************************

class TinyMCEMemo2x2AndroidMainWidget(BaseDashboardPluginWidget):
    """
    TinyMCE memo plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'tinymce_memo_2x2'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('tinymce/render_main.html', context)

# ***************************************************************************
# ****************** Android widgets for Big TinyMCE memo plugin ************
# ***************************************************************************

class TinyMCEMemo3x3AndroidMainWidget(TinyMCEMemo2x2AndroidMainWidget):
    """
    Memo3x3 plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'tinymce_memo_3x3'
    cols = 3
    rows = 3


# ***********************************************************************
# ****************** Windows8 widgets for Memo plugin *******************
# ***********************************************************************

class Memo2x2Windows8MainWidget(BaseDashboardPluginWidget):
    """
    Memo2x2 plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'memo_2x2'
    cols = 2
    rows = 2

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_main.html', context)


class Memo2x2Windows8SidebarWidget(Memo2x2Windows8MainWidget):
    """
    Memo2x2 plugin widget for Windows8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
    cols = 1
    rows = 1

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('memo/render_shortcuts.html', context)


# ***************************************************************************
# ****************** Windows 8 widgets for Memo3x3 plugin ******************
# ***************************************************************************

class Memo3x3Windows8MainWidget(Memo3x3AndroidMainWidget):
    """
    Memo3x3 plugin widget for Windows8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
