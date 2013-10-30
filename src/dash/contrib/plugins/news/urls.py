from django.conf.urls import patterns, url

urlpatterns = patterns('dash.contrib.plugins.news.views',
    # Listing URL
    url(r'^$', view='browse', name='news.browse'),

    # Detail URL
    url(r'^(?P<slug>(?!overview\-)[\w\-\_\.\,]+)/$', view='detail', name='news.detail'),
)