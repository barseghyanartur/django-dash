=======================================
dash.contrib.apps.public_dashboard
=======================================
Public dashboard micro app for django-dash.

Installation
=======================================
Add "public_dashboard" to ``INSTALLED_APPS``.

>>> INSTALLED_APPS = (
>>>    # ...
>>>    'dash.contrib.apps.public_dashboard',
>>>    # ...
>>> )

Add `public_dashboard` url patterns to projects' main url file.

>>> urlpatterns = patterns('',
>>>     # ...
>>>     url(r'^', include('dash.contrib.apps.public_dashboard.urls')),
>>>     # ...
>>> )
