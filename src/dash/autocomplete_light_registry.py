import autocomplete_light.shortcuts as al

from dash.models import DashboardPlugin

""" For Dash Plugins """
al.register(DashboardPlugin,
    search_fields = ['^plugin_uid'],
    attrs = { 'placeholder': 'Select Plugin...', 'data-autocomplete-minimum-characters': 1, },
    widget_attrs = { 'data-widget-maximum-values': 4, 'class': 'imp-autocomplete', },
)

