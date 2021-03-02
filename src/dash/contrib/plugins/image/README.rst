==========================
dash.contrib.plugins.image
==========================
An image plugin for django-dash. Allows users to place images on their
dashboards.

Installation
============
Installation steps described below.

#) Add ``dash.contrib.plugins.image`` to ``INSTALLED_APPS`` of your Django
   project settings module.

#) From terminal run:

    .. code-block:: sh

        ./manage.py dash_sync_plugins

Tuning
======
There are number of settings you can override in the settings module of your Django project:

- ``DASH_PLUGIN_IMAGE_DEFAULT_FIT_METHOD`` (string): Default fit method.
  Available options are: ``smart``, ``center``, ``scale``, ``fit_width``,
  ``fit_height``.
- ``DASH_PLUGIN_IMAGE_IMAGES_UPLOAD_DIR`` (string): Path to directory where
  the images would be uploaded. Defaults to ``dash-image-plugin-images``.

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
