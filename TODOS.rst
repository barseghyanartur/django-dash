===============================================
TODOs
===============================================
Based on the MoSCoW principle. Must haves and should haves are planned to be worked on.

* Features/issues marked with plus (+) are implemented/solved.
* Features/issues marked with minus (-) are yet to be implemented.

Must haves
===============================================
Core and contrib
-----------------------------------------------
+ Layouts:
    + Android layout.
    + Windows 8 layout.
    + Twitter bootstrap 2.
    - Twitter bootstrap 3.
+ Documentation.
+ Group widgets.
+ Plugins:
    + Memo plugin.
    + URL plugin.
    + RSS feed plugin.
    + Weather plugin.
    + Simple news plugin.
    + Video plugin.
+ Unify the CSS usage, so that colours for font-awesome icons do get the same colour from layout.
+ Apply CSS unifications to News plugin.
+ Public dashboard (visible to everyone).
+ CRUD operations for models ``DashboardSettings``, ``DashboardWorkspace``, ``DashboardEntry`` based
  on Django permissions.
+ Template tags for permissions (edit dashboard, add workspace, etc) and templates properly adjusted.
+ Add extensive logging.
+ Make sure no strange things happen logged in with no administartive privelleges.
+ Fix Internet Explorer bug (layout not centered).
+ When running on Python 3, b'string' like values appear in the front end. Get rid of that!
+ Add authentication templates to the example application.
+ Stand alone templates top menu on click style fix.
+ Basic Django tests.
+ Demo app (installer), which would create records.
+ Log out link.
+ List all (or most important) overridable settings.
+ Add news app to the demo app installer. Create a new workspace on which news app would be shown. Use
  Delusional Insanity images as image factory. Take those images from a bitbucket repository.
+ Add licenses.
+ In the example app, make use of bulk-save.
+ When user is not logged in and log out link is chosen to be shown, show the log in link.
+ Update documentation on what's related to Windows 8 layout placeholders.
+ At the moment, plugin widget UIDs are invalid in terms of HTML (should start with a letter). Fix this.
+ In documentation, link to specific plugin directory on github or code in documentation.
+ Update documentatio in what's related the plugin access rights management.
+ Find out why huge news and rss feed plugin JavaScripts appear on pages where they are not used. Somehow,
  on the first page load, all plugins are loaded correctly, but when user goes to some other page where
  other plugins are used and then goes back to the previous page, the plugin scripts from the initial page
  are still loaded.
+ Make it possible to obtain the layout object by name in the template, in case if user needs some strange
  HTML setup.
+ Get rid of the lines in the layout. Replace them with dots, like on Android or Ubuntu.
+ At the moment, removing of a workspace does trigger removal of its' all dashboard entries, however, it
  doesn't clean-up the plugin data (files or database records), while it should!
+ Ensure, that all files saved have unique filenames!
+ Placeholder cell margins.
+ Add public dashboard hoocks.
+ Make the rest of the menus and dialogues to be shown in the same style as Bootstrap 2 layout (when
  Bootstrap 2 layout is loaded).
+ Limit the number of icons for URL plugin when in Bootstrap layout.
+ Make sure all selenium tests still work after HTML changes.
+ Fix issue with "edit" icon not shown on the widge in edit mode (only "delete" is shown).
- Widgets dialogue in bootstrap style for Bootstrap layout (find a proper theme!).
- Fix bug with public dashboard app not showing entries for `example` layouts. This is actually caused by
  probably not well tested placeholder usage by name in templates.
- Fix Google Chrome bug, when dash widget controls (edit/delete) being hidden under Youtube video.
- Strange problems with hover in IE (all versions).
- Add workspace create/delete/edit tests.
- Add dashboard settings (edit), including the layout change tests.

Should haves
===============================================
Core and contrib
-----------------------------------------------
+ Image plugin (with options to: crop, fit width or fit height).
+ Think of a convention on naming the plugins and widgets.
+ Make installation instructions for all plugins, especially advanced ones (that require to be added
  to ``urls`` module).
+ Now that delusionalinsanity.images is available and downloadable on github, make changes to
  the images grabbing script in such a way, that it no longer requires mercurial or is system
  dependant (just downloads the zip and unpacks it using python built-in shutils).
+ Add `get_width` and `get_height` shortcut methods to the base plugin widget.
+ Add translations for Dutch.
+ Add translations for Russian.
- Add translations for Armenian.
- Plugin and widget factory, for creating plugins and widgets easier (since it's mostly just extending
  some plugin or widget, just changing the name and rows/cols).
- File plugin.
- Add navigation (at right and left) to navigate through the workspaces (like in Android).
- Copy/paste widgets between workspaces.

Could haves
===============================================
Core and contrib
-----------------------------------------------
- Base auto-updated plugins and widgets (using AJAX pull or socket.io).
- Contact form plugin.
- Dragging of widgets (within the Placeholder).
- Reset dashboards triggers/hoocks.
- Pre-defined template system for workspaces (with plugins in).
- Blog application, based on public dashboard concept.
- When blog engine is ready, add notes about using a public site with blogs.
- Ubuntu 12.04 layout.
- Mac layout.
- In-line editing.
- Choose custom image for dashboard workspace background.

Example app
-----------------------------------------------
+ Basic example app with a layout and couple of plugins defined.
- Implemented triggers for resetting the dashboard.

Would haves
===============================================
Core and contrib
-----------------------------------------------
- Share dashboard feature, when user chooses some other users to share his dashboard with. It should most
  likely happen by adding user by email or username.
- Google agenda/calendar plugin.
- Google docs plugin.
- Twitter feed plugin.

Example app
-----------------------------------------------
