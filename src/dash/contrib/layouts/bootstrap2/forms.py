from ....contrib.plugins.url.forms import URLForm

from .settings import IMAGE_CHOICES_WITH_EMPTY_OPTION

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('URLBootstrapTwoForm',)


class URLBootstrapTwoForm(URLForm):
    """URLBootstrapTwoForm.

    Almost like the original, but has less options.
    """
    def __init__(self, *args, **kwargs):
        super(URLBootstrapTwoForm, self).__init__(*args, **kwargs)
        self.fields['image'].choices = IMAGE_CHOICES_WITH_EMPTY_OPTION
