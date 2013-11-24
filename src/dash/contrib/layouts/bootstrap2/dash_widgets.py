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

class Dummy1x1Bootstrap2FluidMainWidget(Dummy1x1AndroidMainWidget):
    """
    Dummy1x1 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'dummy_1x1'


class Dummy2x2Bootstrap2FluidMainWidget(Dummy1x1Bootstrap2FluidMainWidget):
    """
    Dummy2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'dummy_2x2'
    cols = 2
    rows = 2

# *************************************************************
# ***************** Image widgets *****************************
# *************************************************************

class Image1x1Bootstrap2FluidMainWidget(Image1x1AndroidMainWidget):
    """
    Image1x1 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'image_1x1'


class Image2x2Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_2x2'
    cols = 2
    rows = 2


class Image3x2Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image3x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_3x2'
    cols = 3
    rows = 2


class Image3x3Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image3x3 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_3x3'
    cols = 3
    rows = 3


class Image3x4Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image3x4 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_3x4'
    cols = 3
    rows = 4


class Image4x4Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image4x4 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_4x4'
    cols = 4
    rows = 4


class Image4x5Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image4x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_4x5'
    cols = 4
    rows = 5


class Image5x4Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image5x4 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_5x4'
    cols = 5
    rows = 4


class Image5x5Bootstrap2FluidMainWidget(Image1x1Bootstrap2FluidMainWidget):
    """
    Image5x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'image_5x5'
    cols = 5
    rows = 5

# *************************************************************
# ***************** Memo widgets *****************************
# *************************************************************

class Memo2x2Bootstrap2FluidMainWidget(Memo2x2AndroidMainWidget):
    """
    Memo2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'memo_2x2'


class Memo3x3Bootstrap2FluidMainWidget(Memo2x2Bootstrap2FluidMainWidget):
    """
    Memo3x3 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'memo_3x3'
    cols = 3
    rows = 3


class Memo4x5Bootstrap2FluidMainWidget(Memo2x2Bootstrap2FluidMainWidget):
    """
    Memo4x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'memo_4x5'
    cols = 4
    rows = 5


class Memo5x5Bootstrap2FluidMainWidget(Memo2x2Bootstrap2FluidMainWidget):
    """
    Memo5x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'memo_5x5'
    cols = 5
    rows = 5


class TinyMCE2x2Bootstrap2FluidMainWidget(TinyMCEMemo2x2AndroidMainWidget):
    """
    Dummy2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    plugin_uid = 'tinymce_memo_2x2'
    placeholder_uid = 'main'
    cols = 2
    rows = 2


class TinyMCE3x3Bootstrap2FluidMainWidget(TinyMCE2x2Bootstrap2FluidMainWidget):
    """
    Dummy2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'tinymce_memo_3x3'
    cols = 3
    rows = 3


class TinyMCE4x4Bootstrap2FluidMainWidget(TinyMCE2x2Bootstrap2FluidMainWidget):
    """
    TinyMCE 4x4 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'tinymce_memo_4x4'
    cols = 4
    rows = 4


class TinyMCE5x5Bootstrap2FluidMainWidget(TinyMCE2x2Bootstrap2FluidMainWidget):
    """
    TinyMCE 5x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'tinymce_memo_5x5'
    cols = 5
    rows = 5

# *************************************************************
# ******************* URL widgets *****************************
# *************************************************************

class URLBootstrapTwo1x1Bootstrap2FluidMainWidget(URL1x1AndroidMainWidget):
    """
    URL1x1 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'url_bootstrap_two_1x1'
    media_css = (
        'css/dash_plugin_url_bootstrap2.css',
    )


class URLBootstrapTwo2x2Bootstrap2FluidMainWidget(URLBootstrapTwo1x1Bootstrap2FluidMainWidget):
    """
    URL2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'url_bootstrap_two_2x2'
    cols = 2
    rows = 2

# *************************************************************
# ******************* Video widgets ***************************
# *************************************************************

class Video2x2Bootstrap2FluidMainWidget(Video2x2AndroidMainWidget):
    """
    Video1x1 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    layout_uid = 'bootstrap2_fluid'
    placeholder_uid = 'main'
    plugin_uid = 'video_2x2'


class Video3x3Bootstrap2FluidMainWidget(Video2x2Bootstrap2FluidMainWidget):
    """
    Video2x2 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'video_3x3'
    cols = 3
    rows = 3


class Video4x4Bootstrap2FluidMainWidget(Video2x2Bootstrap2FluidMainWidget):
    """
    Video4x4 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'video_4x4'
    cols = 4
    rows = 4


class Video5x5Bootstrap2FluidMainWidget(Video2x2Bootstrap2FluidMainWidget):
    """
    Video5x5 plugin widget for Bootstrap 2 Fluid layout (placeholder `main`).
    """
    plugin_uid = 'video_5x5'
    cols = 5
    rows = 5
