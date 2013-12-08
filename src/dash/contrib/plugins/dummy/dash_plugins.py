__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BaseDummyPlugin',)

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory
from dash.contrib.plugins.dummy.forms import DummyForm, DummyShortcutsForm

# ********************************************************************************
# ***************************** Base  Dummy plugin *******************************
# ********************************************************************************
class BaseDummyPlugin(BaseDashboardPlugin):
    """
    Base dummy plugin.
    """
    name = _("Dummy")
    form = DummyForm
    group = _("Dummy")

    def get_form(self):
        if 'sidebar' == self.placeholder:
            return DummyShortcutsForm
        else:
            return DummyForm

    def post_processor(self):
        """
        If no text available, use dummy.
        """
        if not self.data.text:
            self.data.text = 'Dummy content'

# ********************************************************************************
# ********** Generating and registering the plugins using factory ****************
# ********************************************************************************
sizes = (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

plugin_factory(BaseDummyPlugin, 'dummy', sizes)
