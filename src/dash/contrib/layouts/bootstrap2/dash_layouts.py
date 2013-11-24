__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Bootstrap2FluidLayout',)

from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder, layout_registry

# *******************************************************************
# ******************** Bootstrap 2 Fluid layout *********************
# *******************************************************************

class Bootstrap2FluidMainPlaceholder(BaseDashboardPlaceholder):
    """
    Main placeholder.
    """
    uid = 'main'
    cols = 11
    rows = 9
    cell_width = 70
    cell_height = 40
    cell_margin_top = 8
    cell_margin_right = 8
    cell_margin_bottom = 8
    cell_margin_left = 8
    edit_template_name = 'bootstrap2/fluid_base_placeholder_edit.html'


class Bootstrap2FluidLayout(BaseDashboardLayout):
    """
    Bootstrap 2 Fluid layout.
    """
    uid = 'bootstrap2_fluid'
    name = 'Bootstrap 2 Fluid'
    view_template_name = 'bootstrap2/fluid_view_layout.html'
    edit_template_name = 'bootstrap2/fluid_edit_layout.html'
    form_snippet_template_name = 'bootstrap2/snippets/generic_form_snippet.html'
    placeholders = [Bootstrap2FluidMainPlaceholder,]
    cell_units = 'px'
    media_css = (
        'css/bootstrap.css',
        'css/dash_layout_bootstap2_fluid.css',
        #'css/dash_solid_borders.css',
    )
    media_js = (
        'js/bootstrap.js',
        'js/dash_layout_bootstap2_fluid.js',
    )

    def get_view_template_name(self, request=None, origin=None):
        """
        Override the master view template for public dashboard app.
        """
        if 'dash.public_dashboard' == origin:
            return 'bootstrap2/fuild_public_dashboard_view_layout.html'
        else:
            return super(Bootstrap2FluidLayout, self).get_view_template_name(request=request, origin=origin)


layout_registry.register(Bootstrap2FluidLayout)
