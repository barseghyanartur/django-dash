from dash.contrib.plugins.dummy.dash_widgets import (
    Dummy1x1Widget,
    Dummy2x2Widget
)
from dash.contrib.plugins.image.dash_widgets import (
    BaseImageWidget,
    Image1x1Widget,
    Image2x2Widget,
    Image3x2Widget,
    Image3x3Widget,
)
from dash.contrib.plugins.memo.dash_widgets import (
    Memo2x2Widget,
    Memo3x3Widget,
    TinyMCEMemo2x2Widget,
    TinyMCEMemo3x3Widget,
)
from dash.contrib.plugins.url.dash_widgets import (
    URL1x1Widget,
    URL2x2Widget,
)
from dash.contrib.plugins.video.dash_widgets import (
    Video2x2Widget,
    Video3x3Widget,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'

# *************************************************************
# ***************** Dummy widgets *****************************
# *************************************************************


class Dummy1x1ExampleMainWidget(Dummy1x1Widget):
    """Dummy1x1 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Dummy2x2ExampleMainWidget(Dummy2x2Widget):
    """Dummy2x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Dummy1x1ExampleTopShortcutsWidget(Dummy1x1Widget):
    """Dummy1x1 plugin widget for Example layout.

    For placeholder `top_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'top_shortcuts'


class Dummy1x1ExampleRightShortcutsWidget(Dummy1x1Widget):
    """Dummy1x1 plugin widget for Example layout.

    For placeholder `right_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'right_shortcuts'


class Dummy2x2ExampleRightShortcutsWidget(Dummy2x2Widget):
    """
    Dummy2x2 plugin widget for Example layout.

    For placeholder `right_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'right_shortcuts'


class Dummy1x1ExampleBottomShortcutsWidget(Dummy1x1Widget):
    """Dummy1x1 plugin widget for Example layout.

    For placeholder `bottom_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'bottom_shortcuts'


class Dummy1x1ExampleLeftShortcutsWidget(Dummy1x1Widget):
    """Dummy1x1 plugin widget for Example layout.

    For placeholder `left_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'left_shortcuts'


class Dummy2x2ExampleLeftShortcutsWidget(Dummy2x2Widget):
    """Dummy2x2 plugin widget for Example layout.

    For placeholder `left_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'left_shortcuts'

# *************************************************************
# ***************** Image widgets *****************************
# *************************************************************


class Image1x1ExampleMainWidget(Image1x1Widget):
    """Image1x1 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Image2x2ExampleMainWidget(Image2x2Widget):
    """Image2x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Image3x2ExampleMainWidget(Image3x2Widget):
    """Image3x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Image3x3ExampleMainWidget(Image3x3Widget):
    """Image3x3 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Image3x8ExampleLeftShortcutsWidget(BaseImageWidget):
    """Image3x8 plugin widget for Example layout.

    For placeholder `left_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'left_shortcuts'
    plugin_uid = 'image_3x8'
    cols = 3
    rows = 8


class Image3x8ExampleRightShortcutsWidget(Image3x8ExampleLeftShortcutsWidget):
    """Image3x8 plugin widget for Example layout.

    For placeholder `right_shortcuts`.
    """

    placeholder_uid = 'right_shortcuts'


class Image8x1ExampleTopShortcutsWidget(BaseImageWidget):
    """Image8x1 plugin widget for Example layout.

    For placeholder `top_shortcuts`."""

    layout_uid = 'example'
    placeholder_uid = 'top_shortcuts'
    plugin_uid = 'image_8x1'
    cols = 8
    rows = 1


class Image8x1ExampleBottomShortcutsWidget(Image8x1ExampleTopShortcutsWidget):
    """Image8x1 plugin widget for Example layout.

    For placeholder `bottom_shortcuts`.
    """
    placeholder_uid = 'bottom_shortcuts'

# *************************************************************
# ***************** Memo widgets *****************************
# *************************************************************


class Memo2x2ExampleMainWidget(Memo2x2Widget):
    """Memo2x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class Memo3x3ExampleMainWidget(Memo3x3Widget):
    """Memo3x3 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class TinyMCE2x2ExampleMainWidget(TinyMCEMemo2x2Widget):
    """Dummy2x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'


class TinyMCE3x3ExampleMainWidget(TinyMCEMemo3x3Widget):
    """Dummy2x2 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'

# *************************************************************
# ******************* URL widgets *****************************
# *************************************************************


class URL1x1ExampleMainWidget(URL1x1Widget):
    """URL1x1 plugin widget for Example layout (placeholder `main`)."""

    layout_uid = 'example'
    placeholder_uid = 'main'

    media_css = (
        'css/dash_plugin_url_example.css',
    )


class URL2x2ExampleLeftShortcutsWidget(URL2x2Widget):
    """URL2x2 plugin widget for Example layout.

    For placeholder `left_shortcuts`.
    """

    layout_uid = 'example'
    placeholder_uid = 'left_shortcuts'

    media_css = (
        'css/dash_plugin_url_example.css',
    )


class URL2x2ExampleRightShortcutsWidget(URL2x2ExampleLeftShortcutsWidget):
    """URL2x2 plugin widget for Example layout.

    For placeholder `right_shortcuts`.
    """

    placeholder_uid = 'right_shortcuts'


class URL2x2ExampleMainWidget(URL2x2Widget):
    """URL2x2 plugin widget for Example layout.

    For placeholder `main`.
    """

    layout_uid = 'example'
    placeholder_uid = 'main'

    media_css = (
        'css/dash_plugin_url_example.css',
    )

# *************************************************************
# ******************* Video widgets ***************************
# *************************************************************


class Video2x2ExampleMainWidget(Video2x2Widget):
    """Video1x1 plugin widget for Example layout.

    For placeholder `main`.
    """

    layout_uid = 'example'
    placeholder_uid = 'main'


class Video3x3ExampleMainWidget(Video3x3Widget):
    """Video2x2 plugin widget for Example layout.

    For placeholder `main`.
    """

    layout_uid = 'example'
    placeholder_uid = 'main'
