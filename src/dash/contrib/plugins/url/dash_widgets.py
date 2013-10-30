__all__ = ('URLAndroidMainWidget', 'URLAndroidShortcutWidget', 'URLWindows8MainWidget', 'URLWindows8SidebarWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# ****************** Android widgets for URL plugin ********************
# **********************************************************************

class URLAndroidMainWidget(BaseDashboardPluginWidget):
    """
    URL plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'url'
    cols = 1
    rows = 1
    media_css = (
        'css/dash_plugin_url_android.css',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('url/render_main.html', context)


class URLAndroidShortcutWidget(URLAndroidMainWidget):
    """
    URL plugin widget for Android layout (placeholder `shortcuts`).
    """
    placeholder_uid = 'shortcuts'
    cols = 1
    rows = 1

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('url/render_shortcuts.html', context)


# **********************************************************************
# ****************** Windows 8 widgets for URL plugin ******************
# **********************************************************************

class URLWindows8MainWidget(BaseDashboardPluginWidget):
    """
    URL plugin widget for Windows 8 layout (placeholder `main`).
    """
    layout_uid = 'windows8'
    placeholder_uid = 'main'
    plugin_uid = 'url'
    cols = 1
    rows = 1
    media_css = (
        'css/dash_plugin_url_windows8.css',
    )

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('url/render_main.html', context)


class URLWindows8SidebarWidget(URLWindows8MainWidget):
    """
    URL plugin widget for Windows 8 layout (placeholder `sidebar`).
    """
    placeholder_uid = 'sidebar'
