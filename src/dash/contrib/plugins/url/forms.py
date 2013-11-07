__all__ = ('URLForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase
from dash.widgets import BooleanRadioSelect
from dash.contrib.plugins.url.settings import IMAGE_CHOICES_WITH_EMPTY_OPTION

class URLForm(forms.Form, DashboardPluginFormBase):
    """
    URL form for `URL1x1Plugin` plugin.
    """
    class Media:
        css = {
            'all': ('css/dash_plugin_url_form.css',)
        }
        js = ('js/dash_plugin_url_form.js',)

    plugin_data_fields = [
        ("title", ""),
        ("url", ""),
        ("external", False),
        ("image", "")
    ]

    title = forms.CharField(label=_("Title"), required=True)
    url = forms.URLField(label=_("URL"), required=True)
    external = forms.BooleanField(label=_("External?"), required=False, initial=False, widget=BooleanRadioSelect)
    image = forms.ChoiceField(label=_("Image"), required=False, choices=IMAGE_CHOICES_WITH_EMPTY_OPTION)

    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)

        if 'class' in self.fields['image'].widget.attrs:
            self.fields['image'].widget.attrs['class'] += ' image-picker'
        else:
            self.fields['image'].widget.attrs['class'] = 'image-picker'

        