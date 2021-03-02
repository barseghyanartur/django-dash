from django.template.loader import render_to_string

from ....base import BaseDashboardPluginWidget

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseMemoWidget',
    'Memo1x1Widget',
    'Memo2x2Widget',
    'Memo3x3Widget',
    'Memo4x5Widget',
    'Memo5x5Widget',
    'Memo6x6Widget',
    'BaseTinyMCEMemoWidget',
    'TinyMCEMemo2x2Widget',
    'TinyMCEMemo3x3Widget',
    'TinyMCEMemo4x4Widget',
    'TinyMCEMemo5x5Widget',
)

# ***********************************************************************
# ********************** Base widget for Memo plugin ********************
# ***********************************************************************


class BaseMemoWidget(BaseDashboardPluginWidget):
    """Base memo plugin widget."""

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('memo/render.html', context)

# ***********************************************************************
# ********************** Specific widgets for Memo plugin ***************
# ***********************************************************************


class Memo1x1Widget(BaseMemoWidget):
    """Memo 1x1 plugin widget."""

    plugin_uid = 'memo_1x1'
    cols = 1
    rows = 1


class Memo2x2Widget(BaseMemoWidget):
    """Memo 2x2 plugin widget."""

    plugin_uid = 'memo_2x2'
    cols = 2
    rows = 2


class Memo3x3Widget(BaseMemoWidget):
    """Memo 3x3 plugin widget."""

    plugin_uid = 'memo_3x3'
    cols = 3
    rows = 3


class Memo4x5Widget(BaseMemoWidget):
    """Memo 4x5 plugin widget."""

    plugin_uid = 'memo_4x5'
    cols = 4
    rows = 5


class Memo5x5Widget(BaseMemoWidget):
    """Memo 5x5 plugin widget."""

    plugin_uid = 'memo_5x5'
    cols = 5
    rows = 5


class Memo6x6Widget(BaseMemoWidget):
    """Memo 6x6 plugin widget."""

    plugin_uid = 'memo_6x6'
    cols = 6
    rows = 6

# ***********************************************************************
# ********************** Base widget for Memo plugin ********************
# ***********************************************************************


class BaseTinyMCEMemoWidget(BaseDashboardPluginWidget):
    """Base TinyMCE memo plugin widget."""

    def render(self, request=None):
        """Render."""
        context = {'plugin': self.plugin}
        return render_to_string('tinymce/render.html', context)

# ***********************************************************************
# ****************** Specific widgets for TinyMCEMemo plugin ************
# ***********************************************************************


class TinyMCEMemo2x2Widget(BaseTinyMCEMemoWidget):
    """TinyMCE memo 2x2 plugin widget."""

    plugin_uid = 'tinymce_memo_2x2'
    cols = 2
    rows = 2


class TinyMCEMemo3x3Widget(BaseTinyMCEMemoWidget):
    """TinyMCE memo 3x3 plugin widget."""

    plugin_uid = 'tinymce_memo_3x3'
    cols = 3
    rows = 3


class TinyMCEMemo4x4Widget(BaseTinyMCEMemoWidget):
    """TinyMCE memo 4x4 plugin widget."""

    plugin_uid = 'tinymce_memo_4x4'
    cols = 4
    rows = 4


class TinyMCEMemo5x5Widget(BaseTinyMCEMemoWidget):
    """TinyMCE memo 5x5 plugin widget."""

    plugin_uid = 'tinymce_memo_5x5'
    cols = 5
    rows = 5
