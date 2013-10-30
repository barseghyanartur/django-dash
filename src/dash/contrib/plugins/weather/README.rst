==================================
dash.contrib.plugins.weather
==================================
A weather plugin for django-dash. Weather forecasts are taken from `worldweatheronline.com`.

Installation
==================================
Installation steps described below.

1. Add `dash.contrib.plugins.weather` to ``INSTALLED_APPS`` of your django settings.

2. From terminal run

    $ ./manage.py dash_sync_plugins

3. Register yourself at (http://developer.worldweatheronline.com/) and obtain an API key. Add the key
   to settings module of your Django project:

>>> DASH_PLUGIN_WEATHER_API_KEY = 'gjfdkgjdkljglkjljlklgj'

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
