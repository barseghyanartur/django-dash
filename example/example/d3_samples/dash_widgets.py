__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# *************************************************************
# ***************** Base chart widget *************************
# *************************************************************

class BaseChartWidget(BaseDashboardPluginWidget):
    """
    Base chart widget.
    """
    media_js = (
        'js/d3.v3.min.js', # Main D3 script
        'js/d3_bubble_chart.js', # Helper script
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('d3_samples/plugins/render.html', context)

