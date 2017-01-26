=====
TODOs
=====
Based on the MoSCoW principle. Must haves and should haves are planned to be
worked on.

* Features/issues marked with plus (+) are implemented/solved.
* Features/issues marked with minus (-) are yet to be implemented.

Upcoming releases
=================
0.6
---
- Fix bug with lightbox, when last opened URL is remembered by lightbox and
all attempts after that end up calling the same URL.
- Fix layout issues with popups.

0.5
---
- Django 1.8, 1.9 and 1.10 support.
- Remove choices from models to forms to avoid unnecessary migrations.

Must haves
==========

Core and contrib
----------------
+ Layouts:
    + Android layout.
    + Windows 8 layout.
    + Twitter bootstrap 2.
    - Twitter bootstrap 3 (planned in 0.6).
    - Foundation 5 (planned in 0.6).
+ Documentation.
+ Group widgets.
+ Plugins:
    + Memo plugin.
    + URL plugin.
    + RSS feed plugin.
    + Weather plugin.
    + Simple news plugin.
    + Video plugin.
+ Unify the CSS usage, so that colours for font-awesome icons do get the same
  colour from layout.
+ Apply CSS unification to News plugin.
+ Public dashboard (visible to everyone).
+ CRUD operations for models ``DashboardSettings``, ``DashboardWorkspace``, 
  ``DashboardEntry`` based on Django permissions.
+ Template tags for permissions (edit dashboard, add workspace, etc) and
  templates properly adjusted.
+ Add extensive logging.
+ Make sure no strange things happen logged in with no administrative
  privileges.
+ Fix Internet Explorer bug (layout not centered).
+ When running on Python 3, b'string' like values appear in the front end. Get
  rid of that!
+ Add authentication templates to the example application.
+ Stand alone templates top menu on click style fix.
+ Basic Django tests.
+ Demo app (installer), which would create records.
+ Log out link.
+ List all (or most important) overridable settings.
+ Add news app to the demo app installer. Create a new workspace on which news
  app would be shown. Use Delusional Insanity images as image factory. Take
  those images from a bitbucket repository.
+ Add licenses.
+ In the example app, make use of bulk-save.
+ When user is not logged in and log out link is chosen to be shown, show the
  log in link.
+ Update documentation on what's related to Windows 8 layout placeholders.
+ At the moment, plugin widget UIDs are invalid in terms of HTML (should start
  with a letter). Fix this.
+ In documentation, link to specific plugin directory on github or code in
  documentation.
+ Update documentation in what's related the plugin access rights management.
+ Find out why huge news and rss feed plugin JavaScripts appear on pages where 
  they are not used. Somehow, on the first page load, all plugins are loaded
  correctly, but when user goes to some other page where other plugins are
  used and then goes back to the previous page, the plugin scripts from the
  initial page are still loaded.
+ Make it possible to obtain the layout object by name in the template, in 
  case if user needs some strange HTML setup.
+ Get rid of the lines in the layout. Replace them with dots, like on Android
  or Ubuntu.
+ At the moment, removing of a workspace does trigger removal of its' all 
  dashboard entries, however, it doesn't clean-up the plugin data (files or
  database records), while it should!
+ Ensure, that all files saved have unique filenames!
+ Placeholder cell margins.
+ Add public dashboard hooks.
+ Make the rest of the menus and dialogues to be shown in the same style as 
  Bootstrap 2 layout (when Bootstrap 2 layout is loaded).
+ Limit the number of icons for URL plugin when in Bootstrap layout.
+ Make sure all selenium tests still work after HTML changes.
+ Fix issue with "edit" icon not shown on the widget in edit mode (only "delete"
  is shown).
+ Fixed issue when the left gray menu (workspaces) is empty in cases when only 
  default workspace is available.
+ Fix image plugin bug with "Fit width" and "Fit height" resize methods.
+ For each plugin, create base widgets. Further, move all layout specific
  widgets to the layout modules.
+ Widgets dialogue in bootstrap style for Bootstrap layout (find a proper
  theme!).
+ Fix bug with public dashboard app not showing entries for `example` layouts. 
  This is actually caused by probably not well tested placeholder usage by name
  in templates.
+ Allow users to make their workspaces cloneable. Then, some other user could
  clone someone else's workspace to his own.
+ Make plugins cloneable.
+ Refactor plugin widgets. The very base one (size related) should be in plugin 
  specific directory. All layout related things shall be in layout itself. Make
  sure to move layout specific media files (JS/CSS) into layout static
  directory.
+ Add bulk update to Django's admin interface of dash.models.DashboardPlugin, 
  in order to be able to assign rights to certain plugins for users and groups
  at once.
+ Plugin and widget factory, for creating plugins and widgets easier (since 
  it's mostly just extending some plugin or widget, just changing the name and
  rows/cols).
+ Bookmark plugin.
+ Simplify the plugin data update mechanism (when plugin data for certain 
  ``DashboardEntry`` objects shall be updated using
  ``dash.utils.update_plugin_data``).
+ Fix the issue with missing top background image in Django admin.
+ Django 1.7 support.
+ When using unicode characters found in workspace slug, ``django-slug`` raises
  an exception.
+ Copy-paste and cut-paste functionality for widgets (between workspaces).
+ Django 1.8 support.
+ Fix referencing the User model properly.
+ Fix the copy-paste functionality to work for non-admins as well.
- Clean up the documentation.
- Make a quick start.
- Leave the bundled plugins but also release each of them separately (BitBucket,
  GitHub, PyPI) in order to simplify improvements and make it easier to
  modify them as needed.
- Update the screen-shots to reflect the latest changes (copy/paste).
- Fix Google Chrome bug, when dash widget controls (edit/delete) being hidden
  under Youtube video.
- Strange problems with hover in IE (all versions).
- Add workspace create/delete/edit tests.
- Use factory in example layout.
- Check docs and apply factory.
- In Russian not all the text fits nicely into the overlays. For "Bootstrap2"
  layout, all overlays are scrollable and too much text is not a problem. For
  "Android", "Windows8" and "Example" layouts it's an issue. Optimise the CSS
  in such a way, that the overlays are scrollable and heading backgrounds grow
  with text.
- Check all translation messages, as some of them are not properly shown in
  Russian locale.
- Check if it's possible to add plugins without config (without form).
- Rewrite the Javascript and core templates with bootstrap3 in mind. Support
  old themes as well.
- Add information (especially license information) of the third-party apps
  used in the project.
- Test dash with plugin which doesn't have a form. If problems occur, use the
  the yet unreleased ``django-fobi`` approach.
- Add "rem" (and other CSS units) to the list of available cell units.

Should haves
============
Core and contrib
----------------
+ Image plugin (with options to: crop, fit width or fit height).
+ Think of a convention on naming the plugins and widgets.
+ Make installation instructions for all plugins, especially advanced ones (that
  require to be added to ``urls`` module).
+ Now that delusionalinsanity.images is available and downloadable on github, 
  make changes to the images grabbing script in such a way, that it no longer
  requires mercurial or is system dependant (just downloads the zip and unpacks
  it using python built-in shutils).
+ Add `get_width` and `get_height` shortcut methods to the base plugin widget.
+ Add translations for Dutch.
+ Add translations for Russian.
+ Live demo on Heroku.
- Make it possible to use something else than Django's ORM (django-mongoengine,
  SQLAlchemy).
- Add translations for Armenian.
- Add dashboard settings (edit) tests and tests after the changed layout (for
  the bootstrap2 theme).
- File plugin.
- Add navigation (at right and left) to navigate through the workspaces (like
  in Android).
- Allow users to share their workspaces with other users. They would need to
  know someone else's username.
- In bulk change dashboard plugins, make use of fancy widget for the users too.

Could haves
===========
Core and contrib
----------------
- Base auto-updated plugins and widgets (using AJAX pull or socket.io).
- Contact form plugin.
- Dragging of widgets (within the Placeholder).
- Reset dashboards triggers/hooks.
- Pre-defined template system for workspaces (with plugins in).
- Blog application, based on public dashboard concept.
- When blog engine is ready, add notes about using a public site with blogs.
- Ubuntu 12.04 layout.
- Mac layout.
- In-line editing.
- Choose custom image for dashboard workspace background.
- Registry decorators.

Example app
-----------
+ Basic example app with a layout and couple of plugins defined.
- Implemented triggers for resetting the dashboard.

Would haves
===========
Core and contrib
----------------
- Share dashboard feature, when user chooses some other users to share his 
  dashboard with. It should most likely happen by adding user by email or
  username.
- Google agenda/calendar plugin.
- Google docs plugin.
- Twitter feed plugin.

Example app
-----------
