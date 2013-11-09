from django.template.loader import render_to_string

from dash.base import BaseDashboardPluginWidget

# *************************************************************
# ***************** Dummy widgets *****************************
# *************************************************************
class Dummy1x1ExampleMainWidget(BaseDashboardPluginWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'dummy_1x1'

    def render(self, request=None):
        context = {'plugin': self.plugin}
        return render_to_string('dummy/render_main.html', context)

class Dummy2x2ExampleMainWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'dummy_2x2'
    cols = 2
    rows = 2
