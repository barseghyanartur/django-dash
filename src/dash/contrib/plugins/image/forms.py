from django import forms
from django.utils.translation import gettext_lazy as _

from ....base import DashboardPluginFormBase
from ....widgets import BooleanRadioSelect

from .helpers import handle_uploaded_file
from .settings import FIT_METHODS_CHOICES, DEFAULT_FIT_METHOD

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('ImageForm',)


class ImageForm(forms.Form, DashboardPluginFormBase):
    """Image form for `ImagePlugin` plugin."""

    plugin_data_fields = [
        ("title", ""),
        ("image", ""),
        ("fit_method", DEFAULT_FIT_METHOD),
        ("show_link", True)
    ]

    title = forms.CharField(label=_("Title"), required=True)
    image = forms.ImageField(label=_("Image"), required=True)
    fit_method = forms.ChoiceField(label=_("Fit method"),
                                   required=False,
                                   initial=DEFAULT_FIT_METHOD,
                                   choices=FIT_METHODS_CHOICES)
    show_link = forms.BooleanField(label=_("Show link?"),
                                   required=False,
                                   initial=True,
                                   widget=BooleanRadioSelect)

    def save_plugin_data(self, request=None):
        """Saving the plugin data and moving the file."""
        image = self.cleaned_data.get('image', None)
        if image:
            saved_image = handle_uploaded_file(image)
            self.cleaned_data['image'] = saved_image
