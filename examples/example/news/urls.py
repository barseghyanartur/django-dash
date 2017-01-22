from django.conf.urls import url
from news.views import *

urlpatterns = [
    # Listing URL
    url(r'^$', view=browse, name='news.browse'),

    # Detail URL
    url(r'^(?P<slug>(?!overview\-)[\w\-\_\.\,]+)/$', view=detail, \
        name='news.detail'),
]
