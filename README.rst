===============================================
django-dash
===============================================
`django-dash` (later on named Dash) is a customisable, modular dashboard application framework for Django.

Dash allows users to create their own custom dashboards. Supports theming (in Dash themes are called layouts)
and multiple workspaces. Dash comes with extensive pythonic API which allows developers to create new Dash
plugins, as well as to modify bundled ones.

To make a clearer association, think of Android for tablets (shortcuts, widgets and apps) or Windows 8 for
tablets or desktops.

Dash inherits all those concepts and makes it possible to implement a dashboard system for Django
applications with minimal efforts.

Prerequisites
===============================================
- Django 1.5.+
- Python 2.6.8+, 2.7.+, 3.3.+

Key concepts
===============================================
- Each layout (theme) consist of placeholders. Each plugin widget has its' own specific HTML/JavaScript/CSS.
- There might be multiple themes implemented and installed, but only one can be active for a
  certain user. Default layout is chosen system wide, but each user (if has an appropriate permission)
  can choose his preferred layout.
- Placeholder is a space, in which the plugin widgets are placed.
- Placeholders are rectangles consisting of cells. Each placeholder has its' own custom number of
  rows and columns.
- Workspace is just another named dashboard. Users switch between workspaces
  in navigation. Amount of workspaces is unlimited.
- Plugin is a (Django) micro app. Most heavy work should happen in plugin. Plugin may have its' own
  views, urls, etc. Rendering happens with use of plugin widgets.
- Plugin widgets are mainly responsible for rendering of the plugin data. Each plugin widget has
  its' own specific HTML/JavaScript/CSS. A single plugin widget is registered for a triple (layout, placeholder,
  plugin).
- Public dashboard (implemented as a contrib app, which makes it optional) allows users to make their
  workspaces public. If user chooses to make his dashboard public, default workspace becomes public.
  As for non-default workspaces, user can still make each of them private or public.

Main features
===============================================
- Customisable layouts (aka theeming).
- Multiple workspaces.
- Tunable access permissions to plugins.

Installation
===============================================
1. Install latest stable version from PyPI

    $ pip install django-dash

   Or latest stable version from GitHub:

    $ pip install -e git+https://github.com/barseghyanartur/django-dash@stable#egg=django-dash

   Or latest stable version from BitBucket:

    $ pip install -e hg+https://bitbucket.org/barseghyanartur/django-dash@stable#egg=django-dash

2. Add `dash` to ``INSTALLED_APPS`` of the your projects' Django settings. Furthermore, all layouts
   and plugins to be used, shall be added to the ``INSTALLED_APPS`` as well.
   
>>> INSTALLED_APPS = (
>>>     # ...
>>>     'dash',
>>>     'dash.contrib.layouts.android',
>>>     'dash.contrib.layouts.windows8',
>>>     'dash.contrib.plugins.dummy',
>>>     'dash.contrib.plugins.memo',
>>>     'dash.contrib.plugins.news',
>>>     'dash.contrib.plugins.rss_feed',
>>>     'dash.contrib.plugins.url',
>>>     'dash.contrib.plugins.video',
>>>     'dash.contrib.plugins.weather',
>>>     # ...
>>> )

3. Make sure that ``django.core.context_processors.request`` is in ``TEMPLATE_CONTEXT_PROCESSORS``.

Demo
===============================================
In order to be able to quickly evaluate the django-dash, a demo app (with a quick installer) has been created
(works on Ubuntu/Debian, may work on other Linux systems as well, although not guaranteed). Follow the instructions
below for having the demo running within a minute.

Grab the latest `django_dash_example_app_installer.sh`

    $ wget https://raw.github.com/barseghyanartur/django-dash/stable/example/django_dash_example_app_installer.sh

Create a new- or switch to existing- virtual environement, assign execute rights to the installer and run
the `django_dash_example_app_installer.sh`.

    $ chmod +x django_dash_example_app_installer.sh

    $ ./django_dash_example_app_installer.sh

Go to the backend and test the app.

Dashboard:

- URL: http://127.0.0.1:8001/dashboard/
- Admin username: test_admin
- Admin password: test

Django admin interface:

- URL: http://127.0.0.1:8001/administration/
- Admin username: test_admin
- Admin password: test

Take a look at the "example/example/templates" directory for getting a better idea of how to integrate templates
of other apps with into dash templates.

See the documentation for some screen shots http://pythonhosted.org/django-dash/#screenshots

Creating a new layout
===============================================
Dash comes with several bundled layouts. Do check their source code as example.

Let's say, our imaginary layout has two placeholders. One large placeholder for all kinds of widgets
(called `main`) and a tiny one for shortcuts (called `shortcuts`).

Placeholder `main`:

- Single cell size  :  150 x 110 pixels
- Dimensions        :  6 cols, 5 rows

Placeholder `shortcuts`:

- Single cell size  :  60 x 55 pixels
- Dimensions        :  1 cols, 10 rows

See the figure below to get an idea of what placeholders are:

- Placeholder `main` consts of cells from 11 to 56.
- Placeholder `shortcuts` consists of cells from 1 to 10.

A single plugin widget may occupy one or more cells. Plugin widgets are rectangles.

To make it clear, see following cases:

- Plugin widget has 2 cols and 1 row. Then, for example, it may occupy cells (11 and 12).
- Plugin widget has 2 cols and 2 rows. Then, for example, it may occupy cells (11, 12, 21
  and 22).
- Plugin widget has 1 col and 3 rows. Then, for example, it may occupy cells (11, 21 and
  31).
- Plugin widget has 4 cols and 3 rows. Then, for example, it may occupy cells (22, 23, 24,
  25, 32, 33, 34, 35, 42, 43, 44 and 45).

>>>                                  `main`                                `shortcuts`
>>>┌───────────┬───────────┬───────────┬───────────┬───────────┬───────────┐ ┌─────┐
>>>│           │           │           │           │           │           │ │  1  │
>>>│           │           │           │           │           │           │ │     │
>>>│    11     │    12     │    13     │    14     │    15     │    16     │ ├─────┤
>>>│           │           │           │           │           │           │ │  2  │
>>>│           │           │           │           │           │           │ │     │
>>>├───────────┼───────────┼───────────┼───────────┼───────────┼───────────┤ ├─────┤
>>>│           │           │           │           │           │           │ │     │
>>>│           │           │           │           │           │           │ │  3  │
>>>│    21     │    22     │    23     │    24     │    25     │    26     │ ├─────┤
>>>│           │           │           │           │           │           │ │  4  │
>>>│           │           │           │           │           │           │ │     │
>>>├───────────┼───────────┼───────────┼───────────┼───────────┼───────────┤ ├─────┤
>>>│           │           │           │           │           │           │ │     │
>>>│           │           │           │           │           │           │ │  5  │
>>>│    31     │    32     │    33     │    34     │    35     │    36     │ ├─────┤
>>>│           │           │           │           │           │           │ │  6  │
>>>│           │           │           │           │           │           │ │     │
>>>├───────────┼───────────┼───────────┼───────────┼───────────┼───────────┤ ├─────┤
>>>│           │           │           │           │           │           │ │     │
>>>│           │           │           │           │           │           │ │  7  │
>>>│    41     │    42     │    43     │    44     │    45     │    46     │ ├─────┤
>>>│           │           │           │           │           │           │ │  8  │
>>>│           │           │           │           │           │           │ │     │
>>>├───────────┼───────────┼───────────┼───────────┼───────────┼───────────┤ ├─────┤
>>>│           │           │           │           │           │           │ │     │
>>>│           │           │           │           │           │           │ │  9  │
>>>│    51     │    52     │    53     │    54     │    55     │    56     │ ├─────┤
>>>│           │           │           │           │           │           │ │ 10  │
>>>│           │           │           │           │           │           │ │     │
>>>└───────────┴───────────┴───────────┴───────────┴───────────┴───────────┘ └─────┘

There are some rules/guideles you should follow.

Let's assume that layout is named `example`. The layout directory should then have the following
structure.

>>> path/to/layout/example/
>>> ├── static
>>> │   ├── css
>>> │   │   └── dash_layout_example.css # Contains layout-specific CSS
>>> │   ├── images
>>> │   └── js
>>> │       └── dash_layout_example.js # Contains layout specific JavaScripts
>>> ├── templates
>>> │   └── example
>>> │       ├── edit_layout.html # Master edit layout
>>> │       └── view_layout.html # Master view layout
>>> ├── __init__.py
>>> └── dash_layouts.py # Where Layouts and Placeholders are defined and registered

Layout and placeholder classes should be placed in the `dash_layouts.py` file.

Each layout should be put into the ``INSTALLED_APPS`` of your projects' Django settings.

>>> INSTALLED_APPS = (
>>>     # ...
>>>     'path.to.layout.example',
>>>     # ...
>>> )

path/to/layout/example/dash_layouts.py
-----------------------------------------------
Step by step review of a how to create and register a layout and placeholders. Note, that dash
autodiscovers your layouts by name of the file `dash_layouts.py`. The module in which the layouts
are defined, has to be named `dash_layouts.py`.

Required imports.

>>> from dash.base import BaseDashboardLayout, BaseDashboardPlaceholder
>>> from dash.base import layout_registry

Defining the Main placeholder.

>>> class ExampleMainPlaceholder(BaseDashboardPlaceholder):
>>>    uid = 'main' # Unique ID of the placeholder.
>>>    cols = 6 # Number of columns in the placeholder.
>>>    rows = 5 # Number of rows in the placeholder.
>>>    cell_width = 150 # Width of a single cell in the placeholder.
>>>    cell_height = 110 # Height of a single cell in the placeholder.

Defining the Shortcuts placeholder.

>>> class ExampleShortcutsPlaceholder(BaseDashboardPlaceholder):
>>>     uid = 'shortcuts' # UID of the placeholder.
>>>     cols = 1 # Number of columns in the placeholder.
>>>     rows = 10 # Number of rows in the placeholder.
>>>     cell_width = 60 # Width of a single cell in the placeholder.
>>>     cell_height = 55 # Height of a single cell in the placeholder.

Defining and registering the Layout.

>>> class ExampleLayout(BaseDashboardLayout):
>>>     uid = 'example' # Layout UID.
>>>     name = 'Example' # Layout name.
>>>
>>>     # View template. Master template used in view mode.
>>>     view_template_name = 'example/view_layout.html'
>>>
>>>     # Edit template. Master template used in edit mode.
>>>     edit_template_name = 'example/edit_layout.html'
>>>
>>>     # All placeholders listed. Note, that placeholders are rendered in the 
>>>     # order specified here.
>>>     placeholders = [ExampleMainPlaceholder, ExampleShortcutsPlaceholder]
>>>
>>>     # Cell units used in the entire layout. Allowed values are: 'px', 'pt', 
>>>     # 'em' or '%'. In the ``ExampleMainPlaceholder`` cell_width is set to 150.
>>>     #  It means that in this particular case its' actual width would be `150px`.
>>>     cell_units = 'px'
>>>
>>>     # Layout specific CSS.
>>>     media_css = ('css/dash_layout_example.css',)
>>>
>>>     # Layout specific JS.
>>>     media_js = ('js/dash_layout_example.js',)
>>>
>>> # Registering the layout.
>>> layout_registry.register(ExampleLayout)

HTML templates
-----------------------------------------------
You custom layout should be interited from base layout templates (view or edit). Both view and edit
layouts share a lot of things, still edit layout is a bit more "heavy".

- view_layout.html should inherit from "dash/layouts/base_view_layout.html".
- edit_layout.html should inherit from "dash/layouts/base_edit_layout.html".

Both "dash/layouts/base_view_layout.html" and "dash/layouts/base_edit_layout.html" inherit from
"dash/layouts/base_layout.html", which in its' turn inherits from "dash/base.html".

Note, that when rendered to HTML, each Dash template, gets a body class "layout" + layouts' unique
identifier (UID). So, the ``ExampleLayout`` layout would automatically get the class "layout-example".

    <body class="layout-example">

In case of Android layout (UID "android") it would be as follows.

    <body class="layout-android">

Base your layout specific custom CSS on presence of those classes.

Same goes for Placeholders. Each placeholder gets `id_` + placeholders' UID and the classes
"placeholder" and "placeholder-" + placeholders' UID. So, the ``ExampleMainPlaceholder`` would look
as follows.

    <div id="id_main" class="placeholder placeholder-main">

And the ``ExampleShortcutsPlaceholder`` placeholder would look as follows.

    <div id="id_shortcuts" class="placeholder placeholder-shortcuts">

Same goes for plugin widgets. Apart from some other classes that each plugin widget would get for
positioning, it gets the "plugin" and "plugin-" + plugin UID. See the following example (for the
plugin Dummy with UID "dummy"). Each plugin also gets an automatic UID on the moment when rendered.
In the example below it's the "6d06f17d-e142-4f45-b9c1-893c38fc2b01".

<div id="6d06f17d-e142-4f45-b9c1-893c38fc2b01" class="plugin plugin-dummy">

Layout, Placeholder, Plugin and Plugin widget have properties for getting their HTML specific
classes and IDs.

Layout (instance)

>>> layout.html_class

Placeholder (instance)

>>> placeholder.html_id
>>> placeholder.html_class

Plugin (instance)

>>> plugin.html_id
>>> plugin.html_class

Plugin widget (static call)

>>> plugin_widget.html_class # Static one

Creating a new plugin
===============================================
Dash comes with several bundled plugins. Do check their source code as example.

Plugins and Plugin Widgets are easy to create. There are some rules/guideles you should follow
when making a new plugin.

Let's assume that plugin is named `sample_memo`. The plugin directory should then have the
following structure.

Note, that you are advised to prefix all your plugin specific media files with `dash_plugin_` for
the sake of common sense.

>>> path/to/plugin/sample_memo/
>>> ├── static
>>> │   ├── css
>>> │   │   └── dash_plugin_sample_memo.css # Plugin specific CSS
>>> │   ├── images
>>> │   └── js
>>> │       └── dash_plugin_sample_memo.js # Plugin specific JavaScripts
>>> ├── templates
>>> │   └── sample_memo
>>> │       ├── render_main.html # Plugin Widget templ. for `main` Placeholder
>>> │       └── render_short.html # Plugin Widget templ. for `shortcuts` Placeholder
>>> ├── __init__.py
>>> ├── dash_plugins.py # Where Plugins and Widgets are defined and registered
>>> ├── dash_widgets.py # Where the Plugin Widgets are defined
>>> └── forms.py # Plugin configuration form

In some cases, you would need plugin specific overridable settings (see ``dash.contrib.plugins.weather``
plugin as an example. You are advised to write your settings in such a way, that variables of your
Django project settings module would have `DASH_PLUGIN_` prefix.

path/to/plugin/sample_memo/dash_plugins.py
-----------------------------------------------
Step by step review of a how to create and register a plugin and plugin widgets. Note, that dash
autodiscovers your plugins by name of the file `dash_plugins.py`. The module in which the plugins
are defined, has to be named `dash_plugins.py`.

Define and register the plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Required imports.

>>> from dash.base import BaseDashboardPlugin, plugin_registry
>>> from path.to.plugin.sample_memo.forms import SampleMemoForm

Defining the Sample Memo plugin.

>>> class SampleMemoPlugin(BaseDashboardPlugin):
>>>     uid = 'sample_memo' # Plugin UID
>>>     name = _("Memo") # Plugin name
>>>     group = _("Memo") # Group to which the plugin belongs to
>>>     form = SampleMemoForm # Plugin forms are explained later

Registering the Sample Memo plugin.

>>> plugin_registry.register(SampleMemoPlugin)

Register plugin widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Plugin widgets are defined in `dash_widgets.py` module (described later), but registered in the
`dash_plugins.py`, which is autodiscovered by `dash`.

Required imports.

>>> from dash.base import plugin_widget_registry
>>> from path.to.plugin.sample_memo.dash_widgets import (
>>>     SampleMemoExampleMainWidget, SampleMemoExampleShortcutWidget
>>>     )

Registering the Sample Memo plugin widgets for Layout `example`.

>>> plugin_widget_registry.register(SampleMemoExampleMainWidget)
>>> plugin_widget_registry.register(SampleMemoExampleShortcutWidget)

path/to/plugin/sample_memo/dash_widgets.py
-----------------------------------------------
Why to have another file for defining widgets? Just to keep the code clean and less messy, although
you could perfectly define all your plugin widgets in the module `dash_plugins.py`, it's recommended
to keep it separate.

Take into consideration, that `dash_widgets.py` is not an autodiscovered file pattern. All your
plugin widgets should be registered in modules named `dash_plugins.py`.

Required imports.

>>> from django.template.loader import render_to_string
>>> from dash.base import BaseDashboardPluginWidget

Memo plugin widget for Example layout (Placeholder `main`).

>>> class SampleExampleMemoExampleMainWidget(BaseDashboardPluginWidget):
>>>     layout_uid = 'example' # Layout for which the Widget is written
>>>     placeholder_uid = 'main' # Placeholder within the Layout for which
>>>                              # the Widget is written
>>>     plugin_uid = 'sample_memo' # Plugin for which the Widget is written
>>>     cols = 2 # Number of Widget columns
>>>     rows = 2 # Number of Widget rows
>>>
>>>     def render(self, request=None):
>>>         context = {'plugin': self.plugin}
>>>         return render_to_string('sample_memo/render_main.html', context)

Memo plugin widget for Example layout (Placeholder `shortcuts`).

>>> class SampleMemoExampleShortcutWidget(SampleMemoExampleMainWidget):
>>>     placeholder_uid = 'shortcuts'
>>>     cols = 1
>>>     rows = 1
>>>
>>>     def render(self, request=None):
>>>         context = {'plugin': self.plugin}
>>>         return render_to_string('sample_memo/render_shortcuts.html', context)

path/to/plugin/sample_memo/forms.py
-----------------------------------------------
What are the plugin forms? Very simple - if plugin is configurable, it has a form. If you need
to have a custom CSS or a JavaScript included when rendering a speicifc form, use Django's class
Media directive in the form.

Required imports.

>>> from django import forms
>>> from dash.base import DashboardPluginFormBase

Memo form (for `Sample Memo` plugin).

>>> class SampleMemoForm(forms.Form, DashboardPluginFormBase):
>>>     plugin_data_fields = [
>>>         ("title", ""),
>>>         ("text", "")
>>>     ]
>>>
>>>     title = forms.CharField(label=_("Title"), required=False)
>>>     text = forms.CharField(label=_("Text"), required=True, \
>>>                            widget=forms.widgets.Textarea)
>>>
>>>     def __init__(self, *args, **kwargs):
>>>         super(MemoForm, self).__init__(*args, **kwargs)

Now, that everything is ready, make your that both layout and the plugin modules are added to
``INSTALLED_APPS`` for your projects' Django settings.

>>> INSTALLED_APPS = (
>>>     # ...
>>>     'path.to.plugin.sample_memo',
>>>     # ...
>>> )

After it's done, go to terminal and type the following command.

    $ ./manage.py dash_sync_plugins

If your HTTP server is running, you would then be able to access your dashboard.

- View URL: http://127.0.0.1:8000/dashboard/
- Edit URL: http://127.0.0.1:8000/dashboard/edit/

Note, that you have to be logged in, in order to use the dashboard. If your new plugin doesn't
appear, set the ``DASH_DEBUG`` to True in your Django's local settings module, re-run your code
and check console for error notifications.

Permissions
===============================================
Plugin system allows administrators to specify the access rights to every plugin. Dash permissions
are based on Django Users and User Groups.

Management commands
===============================================
There are several management commands.

- `dash_find_broken_dashboard_entries`. Find broken dashboard entries that occur when some plugin which did
  exist in the system, no longer exists.
- `dash_sync_plugins`. Should be ran each time a new plugin is being added to the Dash.
- `dash_update_plugin_data`. A mechanism to update existing plugin data in case if it had become invalid
  after a change in a plugin. In order for it to work, each plugin should implement and ``update`` method,
  in which the data update happens.

Tuning
===============================================
There are number of Dash settings you can override in the settings module of your Django project:

- `DASH_RESTRICT_PLUGIN_ACCESS` (bool): If set to True, (Django) permission system for dash plugins is enabled.
   Defaults to True.
- `DASH_ACTIVE_LAYOUT` (str): Active layout UID. Defaults to "android".
- `DASH_LAYOUT_CELL_UNITS` (str): Allowed values for layout cell units. Defaults to ("em", "px", "pt", "%").
- `DASH_DISPLAY_LOGOUT_LINK` (bool): If set to True, the log out link is shown in the Dash drop-down menu.
  Defaults to True.

For tuning of specific contrib plugin, see the docs in the plugin directory.

Styling tips
===============================================
Font Awesome is used for icons. As a convension, all icons of font-awesome are placed within a span.
Next to their original class, they all should be getting an extra class "iconic". Follow that rule
when making a new layout or a plugin (HTML). It allows to make the styling easy, since icon colours
could be then changed within no time.

Bundled plugins and layouts
===============================================
Dash ships with number of bundled (demo) plugins and layouts that are mainly made to demonstrate its'
abilities. In order to work amoung various layouts (themes), each plugin has a single widget registered
for a single layout. It's possible to unregister a bundled widget and replace it with a custom one.

Bundled plugins
-----------------------------------------------
Below a short overview of the plugins. See README.rst directory of each plugin for details.

- News plugin. Shows how to embed your Django news application (front-end part of it) into a Dash plugin widget.
- Weather plugin. Allows to put a weather widget into dashboard.
- RSS feed plugin. Allows users to put any RSS feed right into the dashboard.
- Memo plugin. Allows users to put short notes on their dashboard.
- URL plugin. Allows users to put links to their dashboard.
- Dummy plugin. Mainly made for quick testing. Still, is perfect example of how to write a plugin and widgets.
- Video plugin. Allows users to put YouTube or Vimeo videos to their dashboard.

Bundled layouts
-----------------------------------------------
Below a short overview of the layouts. See README.rst directory of each layout for details.

- Android (like) layout. Has two placeholders: main (6 cols x 5 rows) and shortcuts (1 col x 10 rows).
- Windows 8 (like) layout. Has one placeholder called main (6 cols x 4 rows).

Naming conventions
===============================================
Although you are free to name your plugins and widgets as want (although, you should comply with PEP
http://www.python.org/dev/peps/pep-0008/#function-names), there are some naming conventions introduced,
that you are recommended to follow.

- TinyExampleWidget: 1x1
- SmallExampleWidget: 2x2
- ExampleWidget: 3x3
- BigExampleWidget: 4x4
- HugeExampleWidget: 5x5
- GiganticExampleWidget: 6x6

When making non-square widgets (2x1, 1x2, 3x1, 1x3), use Portrait and Landscape names.

License
===============================================
GPL 2.0/LGPL 2.1

Support
===============================================
For any issues contact me at the e-mail given in the `Author` section.

Author
===============================================
Artur Barseghyan <artur.barseghyan@gmail.com>
