===============================================
Quick start
===============================================
Tutorial for very quick start with ``django-dash``.

Standard Django installation
===============================================
Example project code available `here
<https://github.com/barseghyanartur/django-dash/tree/master/examples/quick_start>`_.

Installation and configuration
-----------------------------------------------
Install the package in your environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: none

    pip install django-dash

INSTALLED_APPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add ``dash`` core and the plugins to the ``INSTALLED_APPS`` of the your
`settings` module.

1. The core.

.. code-block:: python

    'dash',

2. Layouts. `Android` layout is the default layout. If you have chosen a
   different layout, update the value of ``DASH_ACTIVE_LAYOUT`` accordingly.

.. code-block:: python

    'dash.contrib.layouts.android',

   In dash users can choose which layout (from the list of available ones)
   do they want to use as a default. All available layouts shall be listed in
   settings as well.

.. code-block:: python

    'dash.contrib.layouts.bootstrap2',
    'dash.contrib.layouts.windows8',

3. The plugins. Plugins are like blocks. You are recommended to have
   them all installed. Note, that the following plugins do not have
   additional dependencies, while some others (like
   `news
   <https://github.com/barseghyanartur/django-dash/tree/stable/example/example/news/>`_
   would require additional packages to be installed. If so, make sure to have
   installed and configured those dependencies prior adding the dependant
   add-ons to the `settings` module.

.. code-block:: python

    'dash.contrib.plugins.dummy',
    'easy_thumbnails', # Required by `image` plugin
    'dash.contrib.plugins.image',
    'dash.contrib.plugins.memo',
    'dash.contrib.plugins.rss_feed',
    'dash.contrib.plugins.url',
    'dash.contrib.plugins.video',
    'dash.contrib.plugins.weather',

Putting all together, you would have something like this.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        # Core
        'dash',

        # Layouts
        'dash.contrib.layouts.android',
        'dash.contrib.layouts.bootstrap2',
        'dash.contrib.layouts.windows8',

        # Form field plugins
        'dash.contrib.plugins.dummy',
        'easy_thumbnails', # Required by `image` plugin
        'dash.contrib.plugins.image',
        'dash.contrib.plugins.memo',
        'dash.contrib.plugins.rss_feed',
        'dash.contrib.plugins.url',
        'dash.contrib.plugins.video',
        'dash.contrib.plugins.weather',
        # ...
    )

TEMPLATE_CONTEXT_PROCESSORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add ``django.core.context_processors.request`` to
``TEMPLATE_CONTEXT_PROCESSORS`` of your `settings` module.

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        # ...
        "django.core.context_processors.request",
        # ...
    )

urlpatterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add the following line to ``urlpatterns`` of your `urls` module.

.. code-block:: python

    urlpatterns = patterns('',
        # ...

        # django-dash URLs:
        url(r'^dashboard/', include('dash.urls')),

        # django-dash RSS contrib plugin URLs:
        url(r'^dash/contrib/plugins/rss-feed/', include('dash.contrib.plugins.rss_feed.urls')),

        # django-dash News contrib plugin URLs:
        #url(r'^news/', include('news.urls')),

        # django-dash public dashboards contrib app:
        url(r'^dash/public/', include('dash.contrib.apps.public_dashboard.urls')),

        # Admin URLs
        url(r'^admin/', include(admin.site.urls)),

        # ...
        )

Update the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. First you should be syncing/migrating the database. Depending on your
   Django version and migration app, this step may vary. Typically as follows:

.. code-block:: none

    $ ./manage.py syncdb
    $ ./manage.py migrate

2. Sync installed ``dash`` plugins. Go to terminal and type the following
   command.

.. code-block:: none

    $ ./manage.py dash_sync_plugins

Specify the active layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Specify the active/default layout in your `settings` module.

.. code-block:: python

    DASH_ACTIVE_LAYOUT = 'android'

Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``dash`` has been built with permissions in mind. Every single plugin
is permission based. If user hasn't been given permission to work with a
plugin, he won't be. If you want to switch the permission checks off, set the
value of ``DASH_RESTRICT_PLUGIN_ACCESS`` to False in your `settings` module.

.. code-block:: python

    DASH_RESTRICT_PLUGIN_ACCESS = False

Otherwise, after having completed all the steps above, do log into the
Django administration and assign the permissions (to certain user or a group)
for every single form element or form handler plugin. Bulk assignments work
as well.

- http://yourdomain.com/admin/dash/plugin/

Also, make sure to have the Django model permissions set for following models:

- `fobi.models.FormEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L253>`_
- `fobi.models.FormElementEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L427>`_
- `fobi.models.FormHandlerEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/models.py#L463>`_
- `fobi.contrib.plugins.form_handlers.db_store.models.SavedFormDataEntry
  <https://github.com/barseghyanartur/django-fobi/blob/stable/src/fobi/contrib/plugins/form_handlers/db_store/models.py#L52>`_
