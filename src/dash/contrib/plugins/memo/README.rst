==================================
dash.contrib.plugins.memo
==================================
A memo plugin for django-dash. Allows users to place short texts on their dashboards. There are
two sort of memos implemented:
- Plain text memos.
- WYSIWYG (TinyMCE) memos.

Additional requirements
==================================
See the requirements.txt in current directory.

- django-tinymce

Installation
==================================
Installation steps described below.

1. Add `dash.contrib.plugins.memo` to ``INSTALLED_APPS`` of your Django project settings module.

2. From terminal run

    $ ./manage.py dash_sync_plugins

License
==================================
GPL 2.0/LGPL 2.1

Support
==================================
For any issues contact me at the e-mail given in the `Author` section.

Author
==================================
Artur Barseghyan <artur.barseghyan@gmail.com>
