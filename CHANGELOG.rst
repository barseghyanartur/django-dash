=========================
Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.2).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.2 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.6.1
-----
2021-03-05

- Minor fixes.
- More tests.

0.6
---
2021-03-02

.. note::

    Release dedicated to defenders of Armenia and Artsakh (Nagorno Karabakh)
    and all the victims of Turkish and Azerbaijani aggression.

- Drop support for Django < 2.2.
- Drop support for Python < 3.6.
- Add support for Django 2.2, 3.0 and 3.1.
- Fixes in documentation.

0.5.5
-----
2019-08-06

- Some improvements in Django 1.11 support.

0.5.5
-----
2018-02-09

- Minor fixes.

0.5.4
-----
2017-12-27

- Django 2.0 support (experimental).
- Some work on removing Django < 1.8 code.

0.5.3
-----
2017-09-05

- From now on, URL names for login and logout views are defined in the
  settings, in ``AUTH_LOGIN_URL_NAME`` and ``AUTH_LOGOUT_URL_NAME``
  respectively. Defaults are ``auth_login`` and ``auth_logout`` (as in
  ``django-registration`` package, that most of the developers would be
  using).

0.5.2
-----
2017-03-13

- Fixes in demo.
- Minor fixes.

0.5.1
-----
2017-03-12

- Django 1.11 support.

0.5
---
2017-03-11

This is a transitional release. In upcoming versions support for older
versions of Django (1.5, 1.6 and 1.7) will be dropped.

- From now on it's possible to set a layout for the workspace. It means you
  may have different layouts for various workspaces of the same dashboard.
- Moving static files of Android, Bootstrap2 and Windows8 layouts
  into a separate directory (android, bootstrap2 and windows8 respectively).
- The ``vishap`` package dependency updated to the version 0.1.3 (which
  contained an small yet important fix).
- First discover the plugin modules, then the layouts (was the opposite).
- Remove redundant assets (resulted to smaller package size).
- Added the following templates to the layout definitions for simpler
  further customisation: 'dash/add_dashboard_entry_ajax.html' and
  'dash/edit_dashboard_entry_ajax.html'.
- Better referencing the custom user model in foreign key relations by using
  ``settings.AUTH_USER_MODEL`` instead ``django.contrib.auth.get_user_model``.
- Fix wrong app label of the dummy plugin (``dash.contrib.plugins.dummy``),
  which caused import errors on Django >= 1.7.
- From now on it's possible to localise (translated) URLs.
- Compatibility with Django 1.8/1.9/1.10.
- Remove redundant dependencies. Mention, that some of the plugins do
  have additional dependencies.
- Performing additional checks for collision detection when inserting a new
  plugin.
- Improved autodiscover for Django>=1.7. Fix exception when using a dotted
  path to an ``AppConfig`` in ``INSTALLED_APPS`` (instead of using the path to
  the app).
- Fixed wrongly formed app config labels.
- Minor Python3 improvements.
- Clean up the documentation.
- Make a quick start.
- Upgraded ``jquery.colorbox`` to the latest version (1.6.4).
- Stopped using ``django-localeurl``.
- Stopped using ``django-slim`` for translations.
- PEP8 conform code.
- Use OneToOneField instead of ForeignKey on DashboardSettings module. Remove
  null=True from DashPlugin module users and groups relations in order to
  get rid of Django system warnings. Added necessary migrations.
- Using pytest as test runner. Using coverage.

0.4.13
------
2015-03-20

- Minor fixes.

0.4.12
------
2015-01-08

This release contains a small, yet important fix. You are recommended to
upgrade to this version as soon as possible.

- Improved Django 1.7 support.
- Support for wheel packages.
- Soften requirements.
- Mention the heroku demo app in the docs.
- Fix a mistake in `dash.utils.get_user_plugin_uids` function due to which
  the list of allowed user plugin uids for non-admins was always empty.

0.4.11
------
2014-12-21

- Clipboard module for copy, cut and paste operations.
- Make it possible to provide a template for rendering the plugin widgets
  popup dialogue.
- Improvements in Bootstrap 2 layout (using Bootstrap 2 own accordion instead
  of the one coming with jQuery UI in the plugin widgets popup).
- If `ujson` or `simplejson` are installed, they're used in preference to
  stldib `json` module.
- Minor improvements and fixes.

0.4.10
------
2014-12-10

- Minor fixes in Image plugin.
- Minor fixes in RSS feed plugin.

0.4.9
-----
2014-10-22

- Fixed exceptions raised when unicode characters were used as dashboard
  names.
- Softened setup requirements.
- Moved `dash.contrib.plugins.news` into the `examples.example` example
  project. If you have used it, change the path in your projects'
  `settings.py` module accordingly.
- Documentation improvements.

0.4.8
-----
2014-10-12

- Django 1.7 support.

0.4.7
-----
2014-10-01

- Sort widgets alphabetically.
- UI improvements.

0.4.6
-----
2014-07-09

- Allow custom user model.

0.4.5
-----
2014-05-21

- Added 'rem', 'in', 'cm', 'mm', 'ex' and 'pc' units to the list of available
  units.
- Softened dependencies.

0.4.4
-----
2014-03-26

- Minor fixes.

0.4.3
-----
2013-12-21

- Add Bookmark plugin.
- Improvements (simplification) of the API related to force-updating of plugin 
  data, triggered by developers upon changes in source models, used by certain
  plugins.

0.4.2
-----
2013-12-08

- Fix extra (duplicate) menu appearing on the public dashboard of the "Bootstrap2
  Fluid" layout.

0.4.1
-----
2013-12-08

- Added Dutch and Russian translations for the missing parts.

0.4
---
2013-12-07

While core stayed almost intact, there have been major changes made to plugins
and widgets. If you have written your own plugins and widgets, having inherited
existing ones, review your code before updating to this version. It would be
very simple to migrate, though. All layout specific widgets have been moved to
layout modules, having the plugins only implemented base widgets, which are
used (subclassed) by plugins and widgets specified in layouts. Moreover, a
factory feature for plugins and widgets has been introduced. Take `android`
layout as example.

- Plugin and widget factory added, which decreases the amount of plugin and
  widget code by 90%.
- Dashboard workspace cloning feature added. There are two options. Either 
  clone your own workspace or if someone has marked his workspace as public
  and cloneable, an extra option appears on the public dashboard, which allows
  you to clone given workspace.
- Clone dashboard entry feature added (at the moment, API level only).
- In bootstrap 2 fluid layout, the menu items "Edit dashboard" and
  "View dashboard" swapped positions.
- Default widgets added for all plugins. All existing widgets relocated. If 
  you have inherited from any layout specific widget, you will need to update
  your code.
- Bulk change users and groups in dashboard plugins Django admin interface.
- Weather 1x1 widget which formerly had uid "weather" got changed to 
  "weather_1x1". If you used that widget, you may want to update your database.
- Fixed bug in public dashboard app, when requesting placeholders by their 
  name in the template scope didn't work (while iteration through the
  placeholders did work).

0.3.2
-----
2013-11-24

- Fix image plugin bug occurring with "Fit width" and "Fit height" resize
  methods.

0.3.1
-----
2013-11-24

- Fixed issue when the left gray menu (workspaces) is empty in cases when only 
  default workspace is available.

0.3
---
2013-11-24

- Bootstrap 2 Fluid layout added.
- Fixed permission issue (non-admins not able to edit current workspace).
- Fixed image plugin unique file names issue.
- Fixed bug with placeholder rendering (wrong template chosen).
- Placeholder cell margins definable for each placeholder.
- Customisable form snippets for layouts.
- The very essential core CSS moved to a separate file (dash_core.css).
- Plugin and widget documentation brought in accordance with new naming
  conventions.
- Overall cleanup and improvements.

0.2.4
-----
2013-11-09

- Now when workspace is deleted, the plugin ``delete_plugin_data`` method is
  fired for all dashboard entries so that all the related plugin data is wiped
  as well.
- Move layout borders into separate stylesheet, making it easy to switch
  between those.

0.2.3
-----
2013-11-08

- Making it possible to refer to a placeholder by it's uid in templates.
- Nice example project with example layouts, plugins and widgets.
- Added notes about Django 1.6 support (seems to work, although not yet
  proclaimed to be flawlessly supported).
- Some core improvements.
- Updated demo installer.

0.2.2
-----
2013-11-07

- Fixed bug with string translation (cyrillic) when adding a dashboard widget.
- Russian translations added.

0.2.1
-----
2013-11-07

- Fixed resizing of images in Image widget for Windows 8 layout.

0.2
---
2013-11-07

- Added Image plugin.
- All existing plugin and widget names are brought in accordance with new 
  naming  convention (http://pythonhosted.org/django-dash/#naming-conventions).
  If you're using the old plugins, you're likely want to clean up your
  dashboard and start over.
- Some improvements of core.
- Adding ``get_size``, ``get_width`` and ``get_height`` methods to the plugin
  widget class.

0.1.4
-----
2013-11-05

- Added Dutch translations.
- Better documentation.

0.1.3
-----
2013-11-01

- Fix adding up assets when switching between dashboard workspaces.
- Better documentation.

0.1.2
-----
2013-10-31

- Replace ``DISPLAY_LOGOUT_LINK`` with ``DISPLAY_AUTH_LINK``.
- Better documentation.

0.1.1
-----
2013-10-31

- Adding home page to example project.
- Better documentation.

0.1
---
2013-10-30

- Initial.
