from django.utils.translation import gettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from .dash_widgets import BaseChartWidget
from .forms import ChartForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'

# ****************************************************************************
# ************************** Extended plugins ********************************
# ****************************************************************************


class BaseChartPlugin(BaseDashboardPlugin):
    """Base chart plugin."""

    name = _("Chart")
    group = _("Charts")
    form = ChartForm
    html_classes = ['chartonic']

# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************


sizes = (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5)
)

plugin_factory(BaseChartPlugin, 'chart', sizes)

# ****************************************************************************
# ********************************* Registering widgets **********************
# ****************************************************************************

# Registering chart plugin widgets
plugin_widget_factory(BaseChartWidget,
                      'android',
                      'main',
                      'chart',
                      sizes)
plugin_widget_factory(BaseChartWidget,
                      'windows8',
                      'main',
                      'chart',
                      sizes)
plugin_widget_factory(BaseChartWidget,
                      'bootstrap2_fluid',
                      'main',
                      'chart',
                      sizes)
