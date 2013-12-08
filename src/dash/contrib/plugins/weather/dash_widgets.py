__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseWeatherWidget', 'Weather2x2Widget', 'Weather3x3Widget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# **********************************************************************
# *********************** Base weather widget plugin *******************
# **********************************************************************

class BaseWeatherWidget(BaseDashboardPluginWidget):
    """
    Base weather plugin widget.
    """
    #media_js = [
    #    'js/dash_plugin_weather.js',
    #]
    media_css = [
        'css/dash_plugin_weather.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('weather/render.html', context)

# **********************************************************************
# ************************** Specific widgets **************************
# **********************************************************************

class Weather2x2Widget(BaseWeatherWidget):
    """
    Weather plugin 2x2 widget.
    """
    plugin_uid = 'weather_2x2'
    cols = 2
    rows = 2


class Weather3x3Widget(BaseWeatherWidget):
    """
    Weather plugin 3x3 widget.
    """
    plugin_uid = 'weather_3x3'
    cols = 3
    rows = 3
