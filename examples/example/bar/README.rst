===
bar
===
Example app for ``django-dash``. Contains a chart example plugin.

Installation
============
Installation steps described below.

#) Add ``bar`` to ``INSTALLED_APPS`` of your Django project settings module.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'dash',
            'dash.contrib.layouts.android',
            'dash.contrib.layouts.bootstrap2',
            'dash.contrib.layouts.windows8',
            'dash.contrib.plugins.dummy',
            'dash.contrib.plugins.image',
            'dash.contrib.plugins.memo',
            'dash.contrib.plugins.rss_feed',
            'dash.contrib.plugins.url',
            'dash.contrib.plugins.video',
            'dash.contrib.plugins.weather',
            # ...
            'bar',
            # ...
        )

#) From terminal run

    .. code-block:: sh

        ./manage.py dash_sync_plugins

Usage
=====
#) Add ``Chart`` plugin to your dashboard.

#) Use the following data as Date value:

    .. code-block:: javascript

        ['12/4/2012', '12/5/2012', '12/6/2012', '12/7/2012', '12/8/2012', '12/9/2012', '12/10/2012', '12/11/2012', '12/12/2012']

#) Use the following data as Open value:

    .. code-block:: javascript

        ['12966.45', '12948.96', '13026.19', '14172.37', '13310.11', '14262.06', '12931.22', '12289.30']

License
=======
- The the `Polychart2.js <https://github.com/Polychart/polychart2>`_ (
  JavaScript library) is licensed under
  `Creative Commons 3.0 Attribution & Non-commercial
  <http://creativecommons.org/licenses/by-nc/3.0/>`_.
- To the rest of the code falls under the license of the ``django-dash``.

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
