from ....base import (
    BaseDashboardLayout,
    BaseDashboardPlaceholder,
    layout_registry,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('Windows8Layout',)


class Windows8MainPlaceholder(BaseDashboardPlaceholder):
    """Main placeholder."""

    uid = 'main'
    cols = 6
    rows = 4
    cell_width = 140
    cell_height = 135


class WindowsSidebarPlaceholder(BaseDashboardPlaceholder):
    """Sidebar placeholder."""

    uid = 'sidebar'
    cols = 2
    rows = 4
    cell_width = 140
    cell_height = 135


class Windows8Layout(BaseDashboardLayout):
    """Windows8 layout."""

    uid = 'windows8'
    name = 'Windows 8'
    view_template_name = 'windows8/view_layout.html'
    edit_template_name = 'windows8/edit_layout.html'
    placeholders = [Windows8MainPlaceholder, WindowsSidebarPlaceholder]
    cell_units = 'px'
    media_css = (
        'windows8/css/dash_solid_borders.css',
        'windows8/css/dash_layout_windows8.css',
    )
    # media_js = ('js/dash_layout_windows8.js',)


layout_registry.register(Windows8Layout)
