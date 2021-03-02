============================
dash.contrib.plugins.weather
============================
A weather plugin for django-dash. Weather forecasts are taken from
`worldweatheronline.com <http://worldweatheronline.com>`_.

Installation
============
Installation steps described below.

#) Add ``dash.contrib.plugins.weather`` to ``INSTALLED_APPS`` of your Django
   project settings module.

#) From terminal run:

    .. code-block:: sh

        ./manage.py dash_sync_plugins

#) Register yourself at `developer.worldweatheronline.com
   <http://developer.worldweatheronline.com/>`_ and obtain an API key.
   Add the key to settings module of your Django project:

    .. code-block:: python

        DASH_PLUGIN_WEATHER_API_KEY = 'gjfdkgjdkljglkjljlklgj'

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
