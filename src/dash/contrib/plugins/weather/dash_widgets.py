from django.template.loader import render_to_string

from ....base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseWeatherWidget',
    'Weather2x2Widget',
    'Weather3x3Widget',
)

# **********************************************************************
# *********************** Base weather widget plugin *******************
# **********************************************************************


class BaseWeatherWidget(BaseDashboardPluginWidget):
    """Base weather plugin widget."""

    # media_js = [
    #    'js/dash_plugin_weather.js',
    # ]
    media_css = [
        'css/dash_plugin_weather.css',
    ]

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('weather/render.html', context)

# **********************************************************************
# ************************** Specific widgets **************************
# **********************************************************************


class Weather2x2Widget(BaseWeatherWidget):
    """Weather plugin 2x2 widget."""

    plugin_uid = 'weather_2x2'
    cols = 2
    rows = 2


class Weather3x3Widget(BaseWeatherWidget):
    """Weather plugin 3x3 widget."""

    plugin_uid = 'weather_3x3'
    cols = 3
    rows = 3
