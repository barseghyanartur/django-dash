from django.conf.urls import patterns, url

urlpatterns = patterns('dash.contrib.apps.public_dashboard.views',
    # View public dashboard workspace.
    url(r'^(?P<username>[\w_\-]+)/(?P<workspace>[\w_\-]+)/$', view='public_dashboard', name='dash.public_dashboard'),

    # View public dashboard (no workspace selected == default workspace used).
    url(r'^(?P<username>[\w_\-]+)/$', view='public_dashboard', name='dash.public_dashboard'),
)
