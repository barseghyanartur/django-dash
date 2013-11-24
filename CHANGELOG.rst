Release history
=====================================
0.3.2
-------------------------------------
2013-11-24

- Fix image plugin bug with "Fit width" and "Fit height" resize methods.

0.3.1
-------------------------------------
2013-11-24

- Fixed issue when a gray block is shown in place of the workspaces when just default workspace is
  available.

0.3
-------------------------------------
2013-11-24

- Bootstrap 2 Fluid layout added.
- Fixed issue with permission for non-admins editing current workspace.
- Fixed image plugin unique filenames issue.
- Fixed bug when sometimes a custom template not properly selected when rendering the placeholder.
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