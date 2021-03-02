from dash.base import (
    BaseDashboardLayout,
    BaseDashboardPlaceholder,
    layout_registry
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('ExampleLayout',)


class ExampleMainPlaceholder(BaseDashboardPlaceholder):
    """Main placeholder of the Example layout."""

    uid = 'main'
    cols = 5
    rows = 4
    cell_width = 110
    cell_height = 95


class ExampleLeftShortcutsPlaceholder(BaseDashboardPlaceholder):
    """Left shortcuts placeholder of the Example layout."""

    uid = 'left_shortcuts'
    cols = 3
    rows = 8
    cell_width = 55
    cell_height = 55


class ExampleRightShortcutsPlaceholder(ExampleLeftShortcutsPlaceholder):
    """Right shortcuts placeholder of the Example layout."""

    uid = 'right_shortcuts'


class ExampleTopShortcutsPlaceholder(ExampleLeftShortcutsPlaceholder):
    """Top shortcuts placeholder of the Example layout."""

    uid = 'top_shortcuts'
    cols = 8
    rows = 1
    cell_width = 55
    cell_height = 55


class ExampleBottomShortcutsPlaceholder(ExampleTopShortcutsPlaceholder):
    """Bottom shortcuts placeholder of the Example layout."""

    uid = 'bottom_shortcuts'


class ExampleLayout(BaseDashboardLayout):
    """Example layout."""

    uid = 'example'
    name = 'Example'
    view_template_name = 'foo/layouts/view_layout.html'
    edit_template_name = 'foo/layouts/edit_layout.html'
    placeholders = [
        ExampleTopShortcutsPlaceholder,
        ExampleLeftShortcutsPlaceholder,
        ExampleRightShortcutsPlaceholder,
        ExampleMainPlaceholder,
        ExampleBottomShortcutsPlaceholder
    ]
    cell_units = 'px'
    media_css = (
        'css/dash_dashed_borders.css',
        'css/dash_layout_example.css',
    )
    # media_js = ('js/dash_layout_android.js',)


layout_registry.register(ExampleLayout)
