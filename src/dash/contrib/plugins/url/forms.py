from django import forms
from django.utils.translation import gettext_lazy as _

from ....base import DashboardPluginFormBase
from ....widgets import BooleanRadioSelect

from .settings import IMAGE_CHOICES_WITH_EMPTY_OPTION
from .models import Bookmark

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BookmarkForm',
    'URLForm',
)


class URLForm(forms.Form, DashboardPluginFormBase):
    """URL form for ``BaseURLPlugin`` plugin."""

    class Media(object):
        """Media."""

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
    external = forms.BooleanField(label=_("External?"),
                                  required=False,
                                  initial=False,
                                  widget=BooleanRadioSelect)
    image = forms.ChoiceField(label=_("Image"),
                              required=False,
                              choices=IMAGE_CHOICES_WITH_EMPTY_OPTION)

    def __init__(self, *args, **kwargs):
        super(URLForm, self).__init__(*args, **kwargs)

        if 'class' in self.fields['image'].widget.attrs:
            self.fields['image'].widget.attrs['class'] += ' image-picker'
        else:
            self.fields['image'].widget.attrs['class'] = 'image-picker'


class BookmarkForm(forms.Form, DashboardPluginFormBase):
    """Bookmark form for `BaseBookmarkPlugin` plugin."""

    class Media(object):
        """Media."""

        css = {
            'all': ('css/dash_plugin_url_form.css',)
        }
        js = ('js/dash_plugin_url_form.js',)

    plugin_data_fields = [
        ("bookmark", ""),

        # Handled in `save_plugin_data`.
        ("title", ""),
        ("url", ""),
        ("external", False),
        ("image", "")
    ]

    bookmark = forms.ModelChoiceField(label=_("Bookmark"),
                                      queryset=Bookmark._default_manager.all(),
                                      empty_label=_('---------'),
                                      required=True)

    def save_plugin_data(self, request=None):
        """Save plugin data.

        Saving the plugin data and moving the file.
        """
        bookmark = self.cleaned_data.get('bookmark', None)
        if bookmark:
            # Since it's a ``ModelChoiceField``, we can safely given an ID.
            self.cleaned_data['bookmark'] = bookmark.pk

            # Saving the rest of the fields.
            self.cleaned_data['title'] = bookmark.title
            self.cleaned_data['url'] = bookmark.url
            self.cleaned_data['external'] = bookmark.external
            self.cleaned_data['image'] = bookmark.image
