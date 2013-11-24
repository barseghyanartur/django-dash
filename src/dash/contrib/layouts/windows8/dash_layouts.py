__all__ = ('Windows8Layout',)

from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder, layout_registry


class Windows8MainPlaceholder(BaseDashboardPlaceholder):
    """
    Main placeholder.
    """
    uid = 'main'
    cols = 6
    rows = 4
    cell_width = 140
    cell_height = 135


class WindowsSidebarPlaceholder(BaseDashboardPlaceholder):
    """
    Sidebar placeholder.
    """
    uid = 'sidebar'
    cols = 2
    rows = 4
    cell_width = 140
    cell_height = 135


class Windows8Layout(BaseDashboardLayout):
    """
    Windows8 layout.
    """
    uid = 'windows8'
    name = 'Windows 8'
    view_template_name = 'windows8/view_layout.html'
    edit_template_name = 'windows8/edit_layout.html'
    placeholders = [Windows8MainPlaceholder, WindowsSidebarPlaceholder]
    cell_units = 'px'
    media_css = (
        'css/dash_solid_borders.css',
        'css/dash_layout_windows8.css',
    )
    #media_js = ('js/dash_layout_windows8.js',)


layout_registry.register(Windows8Layout)
