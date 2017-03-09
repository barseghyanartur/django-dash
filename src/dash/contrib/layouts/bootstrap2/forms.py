from ....contrib.plugins.url.forms import URLForm

from .settings import IMAGE_CHOICES_WITH_EMPTY_OPTION

__title__ = 'dash.contrib.layouts.bootstrap2.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('URLBootstrapTwoForm',)


class URLBootstrapTwoForm(URLForm):
    """URLBootstrapTwoForm.

    Almost like the original, but has less options.
    """
    def __init__(self, *args, **kwargs):
        super(URLBootstrapTwoForm, self).__init__(*args, **kwargs)
        self.fields['image'].choices = IMAGE_CHOICES_WITH_EMPTY_OPTION
