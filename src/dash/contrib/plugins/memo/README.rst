=========================
dash.contrib.plugins.memo
=========================
A memo plugin for django-dash. Allows users to place short texts on their
dashboards. There are two sort of memos implemented:

- Plain text memos.
- WYSIWYG (TinyMCE) memos.

Additional requirements
=======================
See the requirements.txt in current directory.

- django-tinymce

Installation
============
Installation steps described below.

#) Add ``dash.contrib.plugins.memo`` to ``INSTALLED_APPS`` of your Django
   project settings module.

#) From terminal run:

    .. code-block:: sh

        ./manage.py dash_sync_plugins

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
