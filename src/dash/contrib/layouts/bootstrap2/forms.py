from dash.contrib.plugins.url.forms import URLForm
from dash.contrib.layouts.bootstrap2.settings import IMAGE_CHOICES_WITH_EMPTY_OPTION

class URLBootstrapTwoForm(URLForm):
    """
    Almost like the original, but has less options.
    """
    def __init__(self, *args, **kwargs):
        super(URLBootstrapTwoForm, self).__init__(*args, **kwargs)
        self.fields['image'].choices = IMAGE_CHOICES_WITH_EMPTY_OPTION

