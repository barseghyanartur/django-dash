from django.urls import re_path as url

from .views import get_feed

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('urlpatterns',)

urlpatterns = [
    url(r'^get_feed/(?P<layout_uid>[\w_]+)/(?P<placeholder_uid>[\w_]+)/'
        r'(?P<plugin_uid>[\w_\-]+)/$',
        view=get_feed,
        name='dash.contrib.plugins.rss_feed.get_feed'),
]
