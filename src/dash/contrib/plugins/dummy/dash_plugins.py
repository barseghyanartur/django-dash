from django.utils.translation import gettext_lazy as _

from ....base import BaseDashboardPlugin
from ....factory import plugin_factory
from .forms import DummyForm, DummyShortcutsForm

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('BaseDummyPlugin',)

# ****************************************************************************
# ***************************** Base  Dummy plugin ***************************
# ****************************************************************************


class BaseDummyPlugin(BaseDashboardPlugin):
    """Base dummy plugin."""

    name = _("Dummy")
    form = DummyForm
    group = _("Dummy")

    def get_form(self):
        """Get form."""
        # This is just to show that it's possible to fetch the form
        # dynamically based on some local attributes. Normally, you
        # would just use the same form and same type of configs.
        if 'sidebar' == self.placeholder:
            return DummyShortcutsForm
        else:
            return DummyForm

    def post_processor(self):
        """If no text available, use dummy."""
        if not self.data.text:
            self.data.text = 'Dummy content'


# ****************************************************************************
# ********** Generating and registering the plugins using factory ************
# ****************************************************************************

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
