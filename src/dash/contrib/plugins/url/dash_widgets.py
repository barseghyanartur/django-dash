from django.template.loader import render_to_string

from ....base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseBookmarkWidget',
    'BaseURLWidget',
    'URL1x1Widget',
    'URL2x2Widget',
)

# **********************************************************************
# ************************* Base URL widget plugin *********************
# **********************************************************************


class BaseURLWidget(BaseDashboardPluginWidget):
    """URL plugin widget."""

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('url/render.html', context)

# **********************************************************************
# ************************* Base Bookmark widget plugin ****************
# **********************************************************************


class BaseBookmarkWidget(BaseDashboardPluginWidget):
    """Bookmark plugin widget."""

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('url/render.html', context)

# **********************************************************************
# ************************** Specific widgets **************************
# **********************************************************************


class URL1x1Widget(BaseURLWidget):
    """URL plugin 1x1 widget."""

    plugin_uid = 'url_1x1'


class URL2x2Widget(BaseURLWidget):
    """URL plugin 2x2 widget."""

    plugin_uid = 'url_2x2'
    cols = 2
    rows = 2
