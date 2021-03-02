==================================
dash.contrib.apps.public_dashboard
==================================
Public dashboard micro app for django-dash.

Installation
============
#) Add ``dash.contrib.apps.public_dashboard`` to ``INSTALLED_APPS`` of your
   Django project settings module.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'dash.contrib.apps.public_dashboard',
            # ...
        )

#) Add ``dash.contrib.apps.public_dashboard`` url patterns to ``urls``
   of your Django project settings module.

    .. code-block:: python

        urlpatterns = [
            # ...
            url(r'^', include('dash.contrib.apps.public_dashboard.urls')),
            # ...
        ]

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
