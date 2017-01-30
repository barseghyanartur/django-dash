from django.conf.urls import url
from dash.contrib.apps.public_dashboard.views import *

urlpatterns = [
    # View public dashboard workspace.
    url(r'^(?P<username>[\w_\-]+)/(?P<workspace>[\w_\-]+)/$', view=public_dashboard, name='dash.public_dashboard'),

    # View public dashboard (no workspace selected == default workspace used).
    url(r'^(?P<username>[\w_\-]+)/$', view=public_dashboard, name='dash.public_dashboard'),
]
