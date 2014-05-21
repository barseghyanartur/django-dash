Release history
=====================================
0.4.5
-------------------------------------
2014-05-21

- Added 'rem', 'in', 'cm', 'mm', 'ex' and 'pc' units to the list of available units.
- Softened dependencies.

0.4.4
-------------------------------------
2014-03-26

- Minor fixes.

0.4.3
-------------------------------------
2013-12-21

- Add Bookmark plugin.
- Improvements (simplification) of the API related to force-updating of plugin data, triggered by
  developers upon changes in source models, used by certain plugins.

0.4.2
-------------------------------------
2013-12-08

- Fix extra (duplicate) menu appearing on the public dashboard of the "Bootstrap2 Fluid" layout.

0.4.1
-------------------------------------
2013-12-08

- Added Dutch and Russian translations for the missing parts.

0.4
-------------------------------------
2013-12-07

While core stayed almost intact, there have been major changes made to plugins and widgets. If you
have written your own plugins and widgets, having inherited existing ones, review your code before
updating to this version. It would be very simple to migrate, though. All layout specific widgets
have been moved to layout modules, having the plugins only implemented base widgets, which are
used (subclassed) by plugins and widgets specified in layouts. Moreover, a factory feature for
plugins and widgets has been introduced. Take `android` layout as example.

- Plugin and widget factory added, which decreases the amount of plugin and widget code by 90%.
- Dashboard workspace cloning feature added. There are two options. Either clone your own workspace or
  if someone has marked his workspace as public and clonable, an extra option appears on the public
  dashboard, which allows you to clone given workspace.
- Clone dashboard entry feature added (at the moment, API level only).
- In bootstrap 2 fluid layout, the menu items "Edit dashboard" and "View dashboard" swapped positions.
- Default widgets added for all plugins. All existing widgets relocated. If you have inherited from
  any layout specific widget, you will need to update your code.
- Bulk change users and groups in dashboard plugins Django admin interface.
- Weather 1x1 widget which formerly had uid "weather" got changed to "weather_1x1". If you used that widget,
  you may want to update your database.
- Fixed bug in public dashboard app, when requesting placeholders by their name in the template scope didn't
  work (while iteration through the placeholders did work).

0.3.2
-------------------------------------
2013-11-24

- Fix image plugin bug occuring with "Fit width" and "Fit height" resize methods.

0.3.1
-------------------------------------
2013-11-24

- Fixed issue when the left gray menu (workspaces) is empty in cases when only default workspace is
  available.

0.3
-------------------------------------
2013-11-24

- Bootstrap 2 Fluid layout added.
- Fixed permission issue (non-admins not able to edit current workspace).
- Fixed image plugin unique filenames issue.
- Fixed bug with placeholder rendering (wrong template chosen).
- Placeholder cell margins definable for each placeholder.
- Customisable form snippets for layouts.
- The very essential core CSS moved to a separate file (dash_core.css).
- Plugin and widget documentation brought in accordance with new naming conventions.
- Overal cleanup and improvements.

0.2.4
-------------------------------------
2013-11-09

- Now when workspace is deleted, the plugin `delete_plugin_data` method is fired for all dashboard entries
  so that all the related plugin data is wiped as well.
- Move layout borders into separate stylesheet, making it easy to switch between those.

0.2.3
-------------------------------------
2013-11-08

- Making it possible to refer to a placeholder by it's uid in templates.
- Nice example project with example layouts, plugins and widgets.
- Added notes about Django 1.6 support (seems to work, although not yet proclaimed to be flawlessly supported).
- Some core improvements.
- Updated demo installer.

0.2.2
-------------------------------------
2013-11-07

- Fixed bug with string translation (cyrillic) when adding a dashboard widget.
- Russian translations added.

0.2.1
-------------------------------------
2013-11-07

- Fixed resizing of images in Image widget for Windows 8 layout.

0.2
-------------------------------------
2013-11-07

- Added Image plugin.
- All existing plugin and widget names are brought in accordance with new naming 
  convention (http://pythonhosted.org/django-dash/#naming-conventions). If you're using the
  old plugins, you're likely want to clean up your dashboard and start over.
- Some improvements of core.
- Adding `get_size`, `get_width` and `get_height` methods to the plugin widget class.

0.1.4
-------------------------------------
2013-11-05

- Added Dutch translations.
- Better documentation.

0.1.3
-------------------------------------
2013-11-01

- Fix adding up assets when switching between dashboard workspaces.
- Better documentation.

0.1.2
-------------------------------------
2013-10-31

- Replace DISPLAY_LOGOUT_LINK with DISPLAY_AUTH_LINK.
- Better documentation.

0.1.1
-------------------------------------
2013-10-31

- Adding home page to example project.
- Better documentation.

0.1
-------------------------------------
2013-10-30

- Initial.