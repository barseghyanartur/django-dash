==================================
news
==================================
Former resident of `dash.contrib`. A simple news plugin for django-dash.
Allows users to place news application on their dashboards. Shows how to
integrate complex applications into Dash widgets.

Additional requirements
==================================
See the requirements.txt in current directory.

- django-tinymce

Installation
==================================
Installation steps described below.

1. Add `news` to ``INSTALLED_APPS`` of your Django
project settings module.

2. From terminal run

.. code-block:: none

    $ ./manage.py dash_sync_plugins

Usage steps
==================================
- In order to quickly be able to evaluate the news plugin, run the following 
  command from your terminal after compelting the installation steps.

.. code-block:: none

    $ ./manage.py news_create_test_data

- Create an admin account and log into the admin section (
  http://127.0.0.1:8000/administration/news/newsitem/) to see the news items
  populated.

- Go to your dashboard and one of available news plugins.

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
