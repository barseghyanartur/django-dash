from django.conf import settings
from django.conf.urls import include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()

url_patterns_args = [
    # django-dash URLs:
    re_path(r'^dashboard/', include('dash.urls')),

    # django-dash RSS contrib plugin URLs:
    re_path(
        r'^dash/contrib/plugins/rss-feed/',
        include('dash.contrib.plugins.rss_feed.urls')
    ),

    # django-dash News contrib plugin URLs:
    re_path(r'^news/', include('news.urls')),

    # django admin
    re_path(r'^administration/', admin.site.urls),

    # django-registration URLs:
    re_path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),

    re_path(r'^$', TemplateView.as_view(template_name='home.html')),

    # django-dash public dashboards contrib app:
    re_path(r'^', include('dash.contrib.apps.public_dashboard.urls')),
]


urlpatterns = i18n_patterns(*url_patterns_args)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if getattr(settings, 'DEBUG', False) \
        and getattr(settings, 'DEBUG_TOOLBAR', False):
    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
