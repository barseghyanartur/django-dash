========================
dash.contrib.plugins.url
========================
A URL plugin for django-dash. Allows users to place links on their dashboards.

Installation
============
Installation steps described below.

#) Add ``dash.contrib.plugins.url`` to ``INSTALLED_APPS`` of your Django
   project settings module.

#) From terminal run

    .. code-block:: sh

        ./manage.py dash_sync_plugins

Tuning
======
There are number of settings you can override in the settings module of your
Django project:

- ``DASH_PLUGIN_URL_IMAGE_CHOICES`` (tuple): Tuple of tuples. Icons available
  in form of (icon-name, icon-title). For full overview of icons see the
  Font `Awesome 3.2.1 docs
  <http://fortawesome.github.io/Font-Awesome/3.2.1/icons/>`_.

For tuning of specific contrib plugin, see the docs in the plugin directory.

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
