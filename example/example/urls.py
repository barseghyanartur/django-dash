from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # django-dash URLs:
    url(r'^dashboard/', include('dash.urls')),

    # django-dash RSS contrib plugin URLs:
    url(r'^dash/contrib/plugins/rss-feed/', include('dash.contrib.plugins.rss_feed.urls')),

    # django-dash News contrib plugin URLs:
    url(r'^dash/contrib/plugins/news/', include('dash.contrib.plugins.news.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^administration/', include(admin.site.urls)),

    # django-registration URLs:
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html')),

    # django-dash public dashboards contrib app:
    url(r'^', include('dash.contrib.apps.public_dashboard.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
