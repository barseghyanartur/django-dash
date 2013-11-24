__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ImageForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase
from dash.widgets import BooleanRadioSelect
from dash.contrib.plugins.image.settings import FIT_METHODS_CHOICES, DEFAULT_FIT_METHOD
from dash.contrib.plugins.image.helpers import handle_uploaded_file

class ImageForm(forms.Form, DashboardPluginFormBase):
    """
    Image form for `ImagePlugin` plugin.
    """
    #class Media:
    #    css = {
    #        'all': ('css/dash_plugin_url_form.css',)
    #    }
    #    js = ('js/dash_plugin_url_form.js',)

    plugin_data_fields = [
        ("title", ""),
        ("image", ""),
        ("fit_method", DEFAULT_FIT_METHOD),
        ("show_link", True)
    ]

    title = forms.CharField(label=_("Title"), required=True)
    image = forms.ImageField(label=_("Image"), required=True)
    fit_method = forms.ChoiceField(label=_("Fit method"), required=False, initial=DEFAULT_FIT_METHOD, \
                                   choices=FIT_METHODS_CHOICES)
    show_link = forms.BooleanField(label=_("Show link?"), required=False, initial=True, widget=BooleanRadioSelect)

    def save_plugin_data(self, request=None):
        """
        Saving the plugin data and moving the file.
        """
        image = self.cleaned_data.get('image', None)
        if image:
            saved_image = handle_uploaded_file(image)
            self.cleaned_data['image'] = saved_image
