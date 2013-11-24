__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Dummy1x1AndroidMainWidget', 'Dummy1x1AndroidShortcutWidget', 'Dummy1x1Windows8MainWidget',
           'Dummy1x1Windows8SidebarWidget', 'Dummy1x2AndroidMainWidget', 'Dummy1x2AndroidShortcutWidget',
           'Dummy2x1AndroidMainWidget', 'Dummy3x3AndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ****************** Android widgets for Dummy plugin ********************
# ************************************************************************

class Dummy1x1AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Dummy plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'dummy_1x1'
    media_js = [
        #'js/dash_plugin_dummy.js',
    ]
    media_css = [
        #'css/dash_plugin_dummy.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('dummy/render_main.html', context)


class Dummy1x1AndroidShortcutWidget(Dummy1x1AndroidMainWidget):
    """
    Dummy plugin widget for Android layout (placeholder `shortcuts`).
    """
    placeholder_uid = 'shortcuts'

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('dummy/render_shortcuts.html', context)

# ************************************************************************
# ****************** Windows8 widgets for Dummy plugin *******************
# ************************************************************************

class Dummy1x1Windows8MainWidget(Dummy1x1AndroidMainWidget):
    """
    Dummy plugin widget for Windows8 (placeholder `main`).
    """
    layout_uid = 'windows8'


class Dummy1x1Windows8SidebarWidget(Dummy1x1Windows8MainWidget):
    """
    Dummy plugin widget for Windows8 (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'

# ************************************************************************
# ****************** Android widgets for Large dummy plugin **************
# ************************************************************************

class Dummy2x1AndroidMainWidget(Dummy1x1AndroidMainWidget):
    """
    Large dummy plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'dummy_2x1'
    cols = 2
    rows = 1

# ************************************************************************
# ************** Android widgets for Large dummy portrait plugin *********
# ************************************************************************

class Dummy1x2AndroidMainWidget(Dummy1x1AndroidMainWidget):
    """
    Large dummy portrait plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'dummy_1x2'
    cols = 1
    rows = 2


class Dummy1x2AndroidShortcutWidget(Dummy1x1AndroidShortcutWidget):
    """
    Large dummy portrait plugin widget for Android (placeholder `shortcuts`).
    """
    plugin_uid = 'dummy_1x2'
    cols = 1
    rows = 2

# ************************************************************************
# ****************** Android widgets for Big dummy plugin ****************
# ************************************************************************

class Dummy3x3AndroidMainWidget(Dummy1x1AndroidMainWidget):
    """
    Big dummy portrait plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'dummy_3x3'
    cols = 3
    rows = 3
