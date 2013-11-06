==================================
dash.contrib.plugins.image
==================================
An image plugin for django-dash. Allows users to place images on their dashboards.

Installation
==================================
Installation steps described below.

1. Add `dash.contrib.plugins.image` to ``INSTALLED_APPS`` of your Django project settings module.

2. From terminal run

    $ ./manage.py dash_sync_plugins

Tuning
===============================================
There are number of settings you can override in the settings module of your Django project:

- `DASH_PLUGIN_URL_IMAGE_CHOICES` (tuple): Tuple of tuples. Icons available in form of (icon-name, icon-title).
  For full overview of icons see the Font Awesome 3.2.1 docs (
  http://fortawesome.github.io/Font-Awesome/3.2.1/icons/).

For tuning of specific contrib plugin, see the docs in the plugin directory.

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
