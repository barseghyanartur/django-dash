from django.conf.urls import url

from .views import public_dashboard

__title__ = 'dash.contrib.apps.public_dashboard.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    # View public dashboard workspace.
    url(r'^(?P<username>[\w_\-]+)/(?P<workspace>[\w_\-]+)/$',
        view=public_dashboard,
        name='dash.public_dashboard'),

    # View public dashboard (no workspace selected == default workspace used).
    url(r'^(?P<username>[\w_\-]+)/$',
        view=public_dashboard,
        name='dash.public_dashboard'),
]
