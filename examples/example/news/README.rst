====
news
====
Former resident of ``dash.contrib``. A simple news plugin for django-dash.
Allows users to place news application on their dashboards. Shows how to
integrate complex applications into Dash widgets.

Additional requirements
=======================
See the requirements.txt in current directory.

- django-tinymce

Installation
============
Installation steps described below.

#) Add ``news`` to ``INSTALLED_APPS`` of your Django project settings module.

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
            'news',
            # ...
        )

#) From terminal run

    .. code-block:: sh

        ./manage.py dash_sync_plugins

Usage steps
===========
#) In order to quickly be able to evaluate the news plugin, run the following
   command from your terminal after completing the installation steps.

    .. code-block:: sh

        ./manage.py news_create_test_data

#) Create an admin account and log into the admin section (
   http://127.0.0.1:8000/administration/news/newsitem/) to see the news items
   populated.

#) Go to your dashboard and one of available news plugins.

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
