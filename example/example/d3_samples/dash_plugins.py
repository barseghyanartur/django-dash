__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from d3_samples.dash_widgets import BaseChartWidget
from d3_samples.forms import ChartForm

# ********************************************************************************
# *************************** Extended plugins ***********************************
# ********************************************************************************

class BaseChartPlugin(BaseDashboardPlugin):
    """
    Base chart plugin.
    """
    name = _("Bubble Chart")
    group = _("D3 plugins")
    form = ChartForm
    html_classes = ['chartonic']

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (5, 5),
    (6, 6),
    (7, 7),
)

plugin_factory(BaseChartPlugin, 'd3_bubble_chart', sizes)

# ********************************************************************************
# ********************************* Registering widgets **************************
# ********************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseChartWidget, 'android', 'main', \
                      'd3_bubble_chart', sizes)
plugin_widget_factory(BaseChartWidget, 'windows8', 'main', \
                      'd3_bubble_chart', sizes)
plugin_widget_factory(BaseChartWidget, 'bootstrap2_fluid', 'main', \
                      'd3_bubble_chart', sizes)
