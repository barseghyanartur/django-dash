from django import forms
from django.utils.translation import gettext_lazy as _

from ....base import DashboardPluginFormBase
from ....widgets import BooleanRadioSelect

from .defaults import (
    DEFAULT_CACHE_FOR,
    DEFAULT_MAX_FEED_ITEMS,
    DEFAULT_SHOW_TITLE,
    DEFAULT_TRUNCATE_AFTER,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('ReadRSSFeedForm',)


class ReadRSSFeedForm(forms.Form, DashboardPluginFormBase):
    """Form for main ``ReadRSSFeedPlugin``."""

    plugin_data_fields = [
        ("feed_url", ""),
        ("custom_feed_title", ""),
        ("show_feed_title", DEFAULT_SHOW_TITLE),
        ("max_items", DEFAULT_MAX_FEED_ITEMS),
        ("truncate_after", DEFAULT_TRUNCATE_AFTER),
        ("cache_for", DEFAULT_CACHE_FOR)
    ]
    feed_url = forms.URLField(label=_("Feed URL"), required=True)
    custom_feed_title = forms.CharField(label=_("Custom feed title"),
                                        required=False)
    show_feed_title = forms.BooleanField(label=_("Show feed title?"),
                                         required=False,
                                         initial=DEFAULT_SHOW_TITLE,
                                         widget=BooleanRadioSelect)
    max_items = forms.IntegerField(label=_("Max feed items to show"),
                                   required=True,
                                   initial=DEFAULT_MAX_FEED_ITEMS)
    truncate_after = forms.IntegerField(label=_("Truncate after"),
                                        required=False,
                                        initial=DEFAULT_TRUNCATE_AFTER)
    cache_for = forms.IntegerField(label=_("Cache for"),
                                   required=True,
                                   initial=DEFAULT_CACHE_FOR)
