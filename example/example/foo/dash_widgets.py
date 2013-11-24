__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from dash.contrib.plugins.dummy.dash_widgets import Dummy1x1AndroidMainWidget
from dash.contrib.plugins.image.dash_widgets import Image1x1AndroidMainWidget
from dash.contrib.plugins.memo.dash_widgets import Memo2x2AndroidMainWidget, TinyMCEMemo2x2AndroidMainWidget
from dash.contrib.plugins.url.dash_widgets import URL1x1AndroidMainWidget
from dash.contrib.plugins.video.dash_widgets import Video2x2AndroidMainWidget

# *************************************************************
# ***************** Dummy widgets *****************************
# *************************************************************

class Dummy1x1ExampleMainWidget(Dummy1x1AndroidMainWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'dummy_1x1'


class Dummy2x2ExampleMainWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'dummy_2x2'
    cols = 2
    rows = 2


class Dummy1x1ExampleTopShortcutsWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `top_shortcuts`).
    """
    placeholder_uid = 'top_shortcuts'


class Dummy1x1ExampleRightShortcutsWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `right_shortcuts`).
    """
    placeholder_uid = 'right_shortcuts'


class Dummy2x2ExampleRightShortcutsWidget(Dummy2x2ExampleMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `right_shortcuts`).
    """
    placeholder_uid = 'right_shortcuts'


class Dummy1x1ExampleBottomShortcutsWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `bottom_shortcuts`).
    """
    placeholder_uid = 'bottom_shortcuts'


class Dummy1x1ExampleLeftShortcutsWidget(Dummy1x1ExampleMainWidget):
    """
    Dummy1x1 plugin widget for Example layout (placeholder `left_shortcuts`).
    """
    placeholder_uid = 'left_shortcuts'

class Dummy2x2ExampleLeftShortcutsWidget(Dummy2x2ExampleMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `left_shortcuts`).
    """
    placeholder_uid = 'left_shortcuts'

# *************************************************************
# ***************** Image widgets *****************************
# *************************************************************

class Image1x1ExampleMainWidget(Image1x1AndroidMainWidget):
    """
    Image1x1 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'image_1x1'


class Image2x2ExampleMainWidget(Image1x1ExampleMainWidget):
    """
    Image2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'image_2x2'
    cols = 2
    rows = 2


class Image3x2ExampleMainWidget(Image1x1ExampleMainWidget):
    """
    Image3x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'image_3x2'
    cols = 3
    rows = 2


class Image3x3ExampleMainWidget(Image1x1ExampleMainWidget):
    """
    Image3x3 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'image_3x3'
    cols = 3
    rows = 3


class Image3x8ExampleLeftShortcutsWidget(Image1x1ExampleMainWidget):
    """
    Image3x8 plugin widget for Example layout (placeholder `main`).
    """
    placeholder_uid = 'left_shortcuts'
    plugin_uid = 'image_3x8'
    cols = 3
    rows = 8


class Image3x8ExampleRightShortcutsWidget(Image3x8ExampleLeftShortcutsWidget):
    """
    Image3x8 plugin widget for Example layout (placeholder `main`).
    """
    placeholder_uid = 'right_shortcuts'


class Image8x1ExampleTopShortcutsWidget(Image1x1ExampleMainWidget):
    """
    Image8x1 plugin widget for Example layout (placeholder `main`).
    """
    placeholder_uid = 'top_shortcuts'
    plugin_uid = 'image_8x1'
    cols = 8
    rows = 1


class Image8x1ExampleBottomShortcutsWidget(Image8x1ExampleTopShortcutsWidget):
    """
    Image8x1 plugin widget for Example layout (placeholder `main`).
    """
    placeholder_uid = 'bottom_shortcuts'

# *************************************************************
# ***************** Memo widgets *****************************
# *************************************************************

class Memo2x2ExampleMainWidget(Memo2x2AndroidMainWidget):
    """
    Memo2x2 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'memo_2x2'


class Memo3x3ExampleMainWidget(Memo2x2ExampleMainWidget):
    """
    Memo3x3 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'memo_3x3'
    cols = 3
    rows = 3


class TinyMCE2x2ExampleMainWidget(TinyMCEMemo2x2AndroidMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    plugin_uid = 'tinymce_memo_2x2'
    placeholder_uid = 'main'
    cols = 2
    rows = 2


class TinyMCE3x3ExampleMainWidget(TinyMCE2x2ExampleMainWidget):
    """
    Dummy2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'tinymce_memo_3x3'
    cols = 3
    rows = 3

# *************************************************************
# ******************* URL widgets *****************************
# *************************************************************

class URL1x1ExampleMainWidget(URL1x1AndroidMainWidget):
    """
    URL1x1 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'url_1x1'


class URL2x2ExampleMainWidget(URL1x1ExampleMainWidget):
    """
    URL2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'url_2x2'
    cols = 2
    rows = 2

# *************************************************************
# ******************* Video widgets ***************************
# *************************************************************

class Video2x2ExampleMainWidget(Video2x2AndroidMainWidget):
    """
    Video1x1 plugin widget for Example layout (placeholder `main`).
    """
    layout_uid = 'example'
    placeholder_uid = 'main'
    plugin_uid = 'video_2x2'


class Video3x3ExampleMainWidget(Video2x2ExampleMainWidget):
    """
    Video2x2 plugin widget for Example layout (placeholder `main`).
    """
    plugin_uid = 'video_3x3'
    cols = 3
    rows = 3
