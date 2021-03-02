from django.utils.translation import gettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from .dash_widgets import (
    BaseBubbleChartWidget,
    BaseStackedToGroupedBarsChartWidget,
    BaseSunburstPartitionChartWidget,
)
from .forms import ChartForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'

# *****************************************************************************
# *************************** Base chart plugin *******************************
# *****************************************************************************


class BaseChartPlugin(BaseDashboardPlugin):
    """Base chart plugin."""

    group = _("D3 plugins")
    form = ChartForm
    html_classes = ['chartonic']


class BaseBubbleChartPlugin(BaseChartPlugin):
    """Base bubble chart plugin."""

    name = _("Bubble Chart")
    html_classes = ['chartonic', 'd3-bubble-chart-plugin']


class BaseStackedToGroupedBarsChartPlugin(BaseChartPlugin):
    """Base stacked-to-grouped bars chart plugin."""

    name = _("Stacked-to-grouped bars chart")
    html_classes = ['chartonic', 'd3-stacked-to-grouped-bars-chart-plugin']


class BaseSunburstPartitionChartPlugin(BaseChartPlugin):
    """Base sunburst partition chart plugin."""

    name = _("Sunburst partition chart")
    html_classes = ['chartonic', 'd3-sunburst-partition-chart-plugin']

# *****************************************************************************
# ********** Generating and registering the plugins using factory *************
# *****************************************************************************


sizes = (
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
)

plugin_factory(BaseBubbleChartPlugin,
               'd3_bubble_chart',
               sizes)
plugin_factory(BaseStackedToGroupedBarsChartPlugin,
               'd3_stacked_to_grouped_bars_chart',
               sizes)
plugin_factory(BaseSunburstPartitionChartPlugin,
               'd3_sunburst_partition_chart',
               sizes)

# *****************************************************************************
# ********************************* Registering widgets ***********************
# *****************************************************************************

# Registering chart plugin widgets

# Bubble Chart
plugin_widget_factory(BaseBubbleChartWidget,
                      'android',
                      'main',
                      'd3_bubble_chart',
                      sizes)
plugin_widget_factory(BaseBubbleChartWidget,
                      'windows8',
                      'main',
                      'd3_bubble_chart',
                      sizes)
plugin_widget_factory(BaseBubbleChartWidget,
                      'bootstrap2_fluid',
                      'main',
                      'd3_bubble_chart',
                      sizes)

# Stacked-to-grouped bars chart
plugin_widget_factory(BaseStackedToGroupedBarsChartWidget,
                      'android',
                      'main',
                      'd3_stacked_to_grouped_bars_chart',
                      sizes)
plugin_widget_factory(BaseStackedToGroupedBarsChartWidget,
                      'windows8',
                      'main',
                      'd3_stacked_to_grouped_bars_chart',
                      sizes)
plugin_widget_factory(BaseStackedToGroupedBarsChartWidget,
                      'bootstrap2_fluid',
                      'main',
                      'd3_stacked_to_grouped_bars_chart',
                      sizes)

# Sunburst Partition
plugin_widget_factory(BaseSunburstPartitionChartWidget,
                      'android',
                      'main',
                      'd3_sunburst_partition_chart',
                      sizes)
plugin_widget_factory(BaseSunburstPartitionChartWidget,
                      'windows8',
                      'main',
                      'd3_sunburst_partition_chart',
                      sizes)
plugin_widget_factory(BaseSunburstPartitionChartWidget,
                      'bootstrap2_fluid',
                      'main',
                      'd3_sunburst_partition_chart',
                      sizes)
