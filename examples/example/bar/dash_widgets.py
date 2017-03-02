from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

# *************************************************************
# ***************** Base chart widget *************************
# *************************************************************


class BaseChartWidget(BaseDashboardPluginWidget):
    """Base chart widget."""

    media_js = (
        'js/polychart2.standalone.js',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'data_date': str(self.plugin.data.data_date),
            'data_open': str(self.plugin.data.data_open),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('bar/plugins/render.html', context)
