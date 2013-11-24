__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ImagePlugin1x1', 'ImagePlugin2x2', 'ImagePlugin3x3', 'ImagePlugin3x2', 'ImagePlugin2x3')

from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin, plugin_registry, plugin_widget_registry
from dash.contrib.plugins.image.forms import ImageForm
from dash.contrib.plugins.image.helpers import delete_file
from dash.contrib.plugins.image.dash_widgets import (
    Image1x1AndroidMainWidget, Image2x2AndroidMainWidget, Image3x3AndroidMainWidget, Image3x2AndroidMainWidget,
    Image2x3AndroidMainWidget
    )
from dash.contrib.plugins.image.dash_widgets import Image1x1Windows8MainWidget, Image1x1Windows8SidebarWidget

# *************************************************************************
# ***************************** Image1x1 plugin ***************************
# *************************************************************************

class Image1x1Plugin(BaseDashboardPlugin):
    """
    Image1x1 dashboard plugin.
    """
    uid = 'image_1x1'
    name = _("Image")
    group = _("Image")
    form = ImageForm
    html_classes = ['pictonic']

    def delete_plugin_data(self):
        """
        Deletes uploaded file.
        """
        delete_file(self.data.image)


plugin_registry.register(Image1x1Plugin)

# *************************************************************************
# ***************************** Image2x2 plugin ***************************
# *************************************************************************

class Image2x2Plugin(Image1x1Plugin):
    """
    Image2x2 dashboard plugin.
    """
    uid = 'image_2x2'

plugin_registry.register(Image2x2Plugin)

# *************************************************************************
# ***************************** Image2x3 plugin ***************************
# *************************************************************************

class Image2x3Plugin(Image1x1Plugin):
    """
    Image2x3 dashboard plugin.
    """
    uid = 'image_2x3'

plugin_registry.register(Image2x3Plugin)

# *************************************************************************
# ***************************** Image3x2 plugin ***************************
# *************************************************************************

class Image3x2Plugin(Image1x1Plugin):
    """
    Image3x2 dashboard plugin.
    """
    uid = 'image_3x2'

plugin_registry.register(Image3x2Plugin)

# *************************************************************************
# ***************************** Image3x3 plugin ***************************
# *************************************************************************

class Image3x3Plugin(Image1x1Plugin):
    """
    Image3x3 dashboard plugin.
    """
    uid = 'image_3x3'

plugin_registry.register(Image3x3Plugin)

# *************************************************************************
# ***************************** Image3x4 plugin ***************************
# *************************************************************************

class Image3x4Plugin(Image1x1Plugin):
    """
    Image3x4 dashboard plugin.
    """
    uid = 'image_3x4'

plugin_registry.register(Image3x4Plugin)

# *************************************************************************
# ***************************** Image4x3 plugin ***************************
# *************************************************************************

class Image4x3Plugin(Image1x1Plugin):
    """
    Image4x3 dashboard plugin.
    """
    uid = 'image_4x3'

plugin_registry.register(Image4x3Plugin)


# *************************************************************************
# ***************************** Image4x4 plugin ***************************
# *************************************************************************

class Image4x4Plugin(Image1x1Plugin):
    """
    Image4x4 dashboard plugin.
    """
    uid = 'image_4x4'

plugin_registry.register(Image4x4Plugin)

# *************************************************************************
# ***************************** Image4x5 plugin ***************************
# *************************************************************************

class Image4x5Plugin(Image1x1Plugin):
    """
    Image4x5 dashboard plugin.
    """
    uid = 'image_4x5'

plugin_registry.register(Image4x5Plugin)


# *************************************************************************
# ***************************** Image5x4 plugin ***************************
# *************************************************************************

class Image5x4Plugin(Image1x1Plugin):
    """
    Image5x4 dashboard plugin.
    """
    uid = 'image_5x4'

plugin_registry.register(Image5x4Plugin)

# *************************************************************************
# ***************************** Image5x5 plugin ***************************
# *************************************************************************

class Image5x5Plugin(Image1x1Plugin):
    """
    Image5x5 dashboard plugin.
    """
    uid = 'image_5x5'

plugin_registry.register(Image5x5Plugin)

# *************************************************************************
# **************** Registering the widgets for Image1x1 plugin ************
# *************************************************************************

# Registering the Android widgets for Image1x1 plugin.
plugin_widget_registry.register(Image1x1AndroidMainWidget)

# Registering the Android widgets for Image1x1 plugin.
plugin_widget_registry.register(Image2x2AndroidMainWidget)

# Registering the Android widgets for Image1x1 plugin.
plugin_widget_registry.register(Image3x3AndroidMainWidget)

# Registering the Android widgets for Image1x1 plugin.
plugin_widget_registry.register(Image3x2AndroidMainWidget)

# Registering the Android widgets for Image1x1 plugin.
plugin_widget_registry.register(Image2x3AndroidMainWidget)

# Registering the Windows8widgets for Image1x1 plugin.
plugin_widget_registry.register(Image1x1Windows8MainWidget)
plugin_widget_registry.register(Image1x1Windows8SidebarWidget)
