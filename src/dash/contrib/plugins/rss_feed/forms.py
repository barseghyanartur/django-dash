__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ReadRSSFeedForm',)

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase
from dash.widgets import BooleanRadioSelect
from dash.contrib.plugins.rss_feed.defaults import DEFAULT_MAX_FEED_ITEMS, DEFAULT_TRUNCATE_AFTER, DEFAULT_CACHE_FOR
from dash.contrib.plugins.rss_feed.defaults import DEFAULT_SHOW_TITLE

class ReadRSSFeedForm(forms.Form, DashboardPluginFormBase):
    """
    Form for main ``ReadRSSFeedPlugin``.
    """
    plugin_data_fields = [
        ("feed_url", ""),
        ("custom_feed_title", ""),
        ("show_feed_title", DEFAULT_SHOW_TITLE),
        ("max_items", DEFAULT_MAX_FEED_ITEMS),
        ("truncate_after", DEFAULT_TRUNCATE_AFTER),
        ("cache_for", DEFAULT_CACHE_FOR)
    ]
    feed_url = forms.URLField(label=_("Feed URL"), required=True)
    custom_feed_title = forms.CharField(label=_("Custom feed title"), required=False)
    show_feed_title = forms.BooleanField(label=_("Show feed title?"), required=False, initial=DEFAULT_SHOW_TITLE, \
                                         widget=BooleanRadioSelect)
    max_items = forms.IntegerField(label=_("Max feed items to show"), required=True, initial=DEFAULT_MAX_FEED_ITEMS)
    truncate_after = forms.IntegerField(label=_("Truncate after"), required=False, initial=DEFAULT_TRUNCATE_AFTER)
    cache_for = forms.IntegerField(label=_("Cache for"), required=True, initial=DEFAULT_CACHE_FOR)
