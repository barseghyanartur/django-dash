__all__ = ('Weather2x2AndroidMainWidget', 'Weather3x3AndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ***********************************************************************
# ****************** Android widgets for Memo plugin ********************
# ***********************************************************************

class Weather2x2AndroidMainWidget(BaseDashboardPluginWidget):
    """
    Weather plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'weather_2x2'
    cols = 2
    rows = 2

    #media_js = [
    #    'js/dash_plugin_weather.js',
    #]
    media_css = [
        'css/dash_plugin_weather.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('weather/render_main.html', context)


# ***************************************************************************
# ****************** Android widgets for Big weather plugin *****************
# ***************************************************************************

class Weather3x3AndroidMainWidget(Weather2x2AndroidMainWidget):
    """
    Big weather plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'weather_3x3'
    cols = 3
    rows = 3
