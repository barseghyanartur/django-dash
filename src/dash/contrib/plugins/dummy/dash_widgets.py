__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseDummyWidget', 'Dummy1x1Widget', 'Dummy1x2Widget', 'Dummy2x1Widget',
    'Dummy2x2Widget', 'Dummy3x3Widget'
)

from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# ************************************************************************
# ************************* Base widget for Dummy plugin *****************
# ************************************************************************

class BaseDummyWidget(BaseDashboardPluginWidget):
    """
    Base dummy plugin widget.
    """
    media_js = [
        #'js/dash_plugin_dummy.js',
    ]
    media_css = [
        #'css/dash_plugin_dummy.css',
    ]

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('dummy/render.html', context)

# ************************************************************************
# ************************* Specific widgets for Dummy plugin ************
# ************************************************************************

class Dummy1x1Widget(BaseDummyWidget):
    """
    1x1 dummy plugin widget.
    """
    plugin_uid = 'dummy_1x1'


class Dummy1x2Widget(BaseDummyWidget):
    """
    1x2 dummy plugin widget.
    """
    plugin_uid = 'dummy_1x2'
    cols = 1
    rows = 2


class Dummy2x1Widget(BaseDummyWidget):
    """
    2x1 dummy plugin widget.
    """
    plugin_uid = 'dummy_2x1'
    cols = 2
    rows = 1


class Dummy2x2Widget(BaseDummyWidget):
    """
    2x2 dummy plugin widget.
    """
    plugin_uid = 'dummy_2x2'
    cols = 2
    rows = 2


class Dummy3x3Widget(BaseDummyWidget):
    """
    3x3 dummy plugin widget.
    """
    plugin_uid = 'dummy_3x3'
    cols = 3
    rows = 3
