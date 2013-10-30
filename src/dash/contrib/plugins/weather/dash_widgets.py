__all__ = ('WeatherAndroidMainWidget', 'BigWeatherAndroidMainWidget')

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ***********************************************************************
# ****************** Android widgets for Memo plugin ********************
# ***********************************************************************

class WeatherAndroidMainWidget(BaseDashboardPluginWidget):
    """
    Weather plugin widget for Android layout (placeholder `main`).
    """
    layout_uid = 'android'
    placeholder_uid = 'main'
    plugin_uid = 'weather'
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

class BigWeatherAndroidMainWidget(WeatherAndroidMainWidget):
    """
    Big memo plugin widget for Android layout (placeholder `main`).
    """
    plugin_uid = 'big_weather'
    cols = 3
    rows = 3
