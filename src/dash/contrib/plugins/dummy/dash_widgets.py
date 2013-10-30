__all__ = ('DummyAndroidMainWidget', 'DummyAndroidShortcutWidget', 'DummyWindows8MainWidget', \
           'DummyWindows8SidebarWidget', 'LargeDummyAndroidMainWidget', \
           'LargeDummyPortraitAndroidMainWidget', 'LargeDummyPortraitAndroidShortcutWidget', \
           'BigDummyAndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ****************** Android widgets for Dummy plugin ********************
# ************************************************************************

class DummyAndroidMainWidget(BaseDashboardPluginWidget):
    """
    Dummy plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'dummy'
    media_js = [
        #'js/dash_plugin_dummy.js',
    ]
    media_css = [
        #'css/dash_plugin_dummy.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('dummy/render_main.html', context)


class DummyAndroidShortcutWidget(DummyAndroidMainWidget):
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

class DummyWindows8MainWidget(DummyAndroidMainWidget):
    """
    Dummy plugin widget for Windows8 (placeholder `main`).
    """
    layout_uid = 'windows8'


class DummyWindows8SidebarWidget(DummyWindows8MainWidget):
    """
    Dummy plugin widget for Windows8 (placeholder `sidebar`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'sidebar'

# ************************************************************************
# ****************** Android widgets for Large dummy plugin **************
# ************************************************************************

class LargeDummyAndroidMainWidget(DummyAndroidMainWidget):
    """
    Large dummy plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'large_dummy'
    cols = 2
    rows = 1

# ************************************************************************
# ****************** Android widgets for Large dummy plugin **************
# ************************************************************************

class LargeDummyPortraitAndroidMainWidget(DummyAndroidMainWidget):
    """
    Large dummy portrait plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'large_dummy_portrait'
    cols = 1
    rows = 2


class LargeDummyPortraitAndroidShortcutWidget(DummyAndroidShortcutWidget):
    """
    Large dummy portrait plugin widget for Android (placeholder `shortcuts`).
    """
    plugin_uid = 'large_dummy_portrait'
    cols = 1
    rows = 2

# ************************************************************************
# ****************** Android widgets for Big dummy plugin ****************
# ************************************************************************

class BigDummyAndroidMainWidget(DummyAndroidMainWidget):
    """
    Big dummy portrait plugin widget for Android (placeholder `main`).
    """
    plugin_uid = 'big_dummy'
    cols = 3
    rows = 3
