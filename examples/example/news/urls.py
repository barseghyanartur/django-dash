from django.conf.urls import url

from .views import browse, detail

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'urlpatterns',
)


urlpatterns = [
    # Listing URL
    url(r'^$', view=browse, name='news.browse'),

    # Detail URL
    url(r'^(?P<slug>(?!overview\-)[\w\-\_\.\,]+)/$',
        view='detail',
        name=detail),
]
