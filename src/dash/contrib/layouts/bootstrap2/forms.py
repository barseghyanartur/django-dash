__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from dash.contrib.plugins.url.forms import URLForm
from dash.contrib.layouts.bootstrap2.settings import IMAGE_CHOICES_WITH_EMPTY_OPTION

class URLBootstrapTwoForm(URLForm):
    """
    Almost like the original, but has less options.
    """
    def __init__(self, *args, **kwargs):
        super(URLBootstrapTwoForm, self).__init__(*args, **kwargs)
        self.fields['image'].choices = IMAGE_CHOICES_WITH_EMPTY_OPTION

