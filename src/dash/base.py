"""
All `uids` are supposed to be pythonic function names (see
PEP http://www.python.org/dev/peps/pep-0008/#function-names).
"""
import copy
import json
import logging
import uuid

from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from .discover import autodiscover
from .exceptions import LayoutDoesNotExist, InvalidRegistryItemType
from .helpers import iterable_to_dict, uniquify_sequence, safe_text

from .settings import (
    ACTIVE_LAYOUT,
    DEBUG,
    DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME,
    DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME,
    LAYOUT_CELL_UNITS,
)

logger = logging.getLogger(__name__)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseDashboardLayout',
    'BaseDashboardPlaceholder',
    'BaseDashboardPlugin',
    'BaseDashboardPluginWidget',
    'DashboardPluginFormBase',
    'PluginWidgetRegistry',
    'collect_widget_media',
    'ensure_autodiscover',
    'get_layout',
    'get_registered_layout_uids',
    'get_registered_layouts',
    'get_registered_plugin_uids',
    'get_registered_plugins',
    'layout_registry',
    'plugin_registry',
    'plugin_widget_registry',
    'validate_placeholder_uid',
    'validate_plugin_uid',
)


class DashboardPluginFormBase:
    """Not a form actually. Defined for magic only.

    :property iterable plugin_data_fields: Fields to get when calling the
        ``get_plugin_data`` method. These field will be JSON serialized. All
        other fields, even if they are part of the form, won't be. Make sure
        all fields are serializable. If some of them aren't, override the
        ``save_plugin_data`` method and make them serializable there. See
        ``dash.contrib.plugins.image.forms`` as a good example.

    :example:

        >>> plugin_data_fields = (
        >>>    ('name', ''),
        >>>    ('active': False)
        >>> )
    """

    plugin_data_fields = None

    def _get_plugin_data(self, fields, request=None):
        """Gets plugin data.

        :param iterable fields: List of tuples to iterate.
        :param django.http.HttpRequest request:
        :return string: JSON dumpled string.
        """
        data = {}

        for field, default_value in fields:
            data.update({field: self.cleaned_data.get(field)})
        return json.dumps(data)

    def get_plugin_data(self, request=None):
        """Data that would be saved in the ``plugin_data`` field of the
        ``dash.models.DashboardEntry`` subclassed model.

        :param django.http.HttpRequest request:
        """
        if self.plugin_data_fields:
            return self._get_plugin_data(self.plugin_data_fields,
                                         request=request)

    def save_plugin_data(self, request=None):
        """Dummy, but necessary."""


class BaseDashboardLayout:
    """Base layout.

    Layouts consist of placeholders.

    :Properties:
        - `uid` (string): Layout unique identifier (globally).
        - `name` (string): Layout name.
        - `description` (string): Layout description.
        - `placeholders` (iterable): Iterable (list, tuple or set)
          of ``dash.base.BaseDashboardPlaceholder` subclasses.
        - `view_template_name` (string): Template used to render the
          layout (view).
        - `edit_template_name` (string): Template used to render the
          layout (edit).
        - `plugin_widgets_template_name_ajax` (string): Template used to
          render the plugin widgets popup.
        - `form_snippet_template_name` (string): Template used to render the
          forms.
        - `html_classes` (string): Extra HTML class that layout should get.
        - `cell_units` (string):
        - `media_css` (list): List all specific stylesheets.
        - `media_js` (list): List all specific javascripts.
    """

    uid = None
    name = None
    description = None
    placeholders = []
    view_template_name = None
    view_template_name_ajax = None
    edit_template_name = None
    edit_template_name_ajax = None
    plugin_widgets_template_name_ajax = 'dash/plugin_widgets_ajax.html'
    form_snippet_template_name = 'dash/snippets/generic_form_snippet.html'

    # 'dash/add_dashboard_entry_ajax.html'
    add_dashboard_entry_template_name = None

    # 'dash/add_dashboard_entry_ajax.html'
    add_dashboard_entry_ajax_template_name = None

    # 'dash/edit_dashboard_entry_ajax.html'
    edit_dashboard_entry_template_name = None

    # 'dash/edit_dashboard_entry_ajax.html'
    edit_dashboard_entry_ajax_template_name = None

    # 'dash/create_dashboard_workspace.html'
    create_dashboard_workspace_template_name = None

    # 'dash/create_dashboard_workspace_ajax.html'
    create_dashboard_workspace_ajax_template_name = None

    # 'dash/edit_dashboard_workspace.html'
    edit_dashboard_workspace_template_name = None

    # 'dash/edit_dashboard_workspace_ajax.html'
    edit_dashboard_workspace_ajax_template_name = None
    html_classes = []

    # Most likely, it makes sense to define this on a layout level.
    # Think of it.
    cell_units = None

    media_css = []
    media_js = []

    def __init__(self, user=None):
        """Constructor.

        :param django.contrib.auth.models.User user:
        """
        assert self.uid
        assert self.name
        assert self.view_template_name
        assert self.edit_template_name
        assert self.placeholders
        assert self.cell_units and self.cell_units in LAYOUT_CELL_UNITS
        assert isinstance(self.media_js, (list, tuple))
        assert isinstance(self.media_css, (list, tuple))

        if isinstance(self.media_js, tuple):
            self.media_js = list(self.media_js)

        if isinstance(self.media_css, tuple):
            self.media_css = list(self.media_css)

        self.placeholders_dict = {}
        self.placeholder_uids = []
        for placeholder in self.placeholders:
            self.placeholders_dict.update({placeholder.uid: placeholder})
            self.placeholder_uids.append(placeholder.uid)

        self.user = user
        self.widget_media_js = []
        self.widget_media_css = []

    def get_view_template_name(self, request=None, origin=None):
        """Get the view template name.

        :param django.http.HttpRequest request:
        :param string origin: Origin of the request. Hook to provide custom
            templates for apps. Example value: 'public_dashboard'. Take the
            `public_dashboard` app as example.
        """
        if not self.view_template_name_ajax:
            return self.view_template_name
        elif request and request.is_ajax():
            return self.view_template_name_ajax
        else:
            return self.view_template_name

    def get_edit_template_name(self, request=None):
        if not self.edit_template_name_ajax:
            return self.edit_template_name
        elif request and request.is_ajax():
            return self.edit_template_name_ajax
        else:
            return self.edit_template_name

    def get_placeholder(self, uid, default=None):
        return self.placeholders_dict.get(uid, default)

    def get_placeholders(self, request=None):
        """Get the list of placeholders registered for the layout.

        :param django.http.HttpRequest request:
        :return iterable: List of placeholder classes. Override in your layout
            if you need a custom behaviour.
        """
        return self.placeholders

    def get_placeholder_uids(self, request=None):
        """Get the list of placeholder uids.

        :param django.http.HttpRequest request:
        :return list:
        """
        uids = []
        for placeholder in self.placeholders:
            uids.append(placeholder.uid)
        return uids

    def collect_widget_media(self, dashboard_entries):
        """Collect the widget media files.

        :param iterable dashboard_entries: Iterable of
            ``dash.models.DashboardEntry`` instances.
        :return list:
        """
        widget_media = collect_widget_media(dashboard_entries)

        if widget_media:
            self.widget_media_js = widget_media['js']
            self.widget_media_css = widget_media['css']

    def get_media_css(self):
        """Get all CSS media files (for the layout + plugins).

        :return list:
        """
        media_css = self.media_css[:]
        if self.widget_media_css:
            media_css += self.widget_media_css

        media_css = uniquify_sequence(media_css)

        return media_css

    def get_media_js(self):
        """Get all JavaScript media files (for the layout + plugins).

        :return list:
        """
        media_js = self.media_js[:]
        if self.widget_media_js:
            media_js += self.widget_media_js

        media_js = uniquify_sequence(media_js)

        return media_js

    def get_grouped_dashboard_entries(self, dashboard_entries):
        """Get dashboard entries grouped by placeholder.

        :param iterable dashboard_entries: Iterable of
            ``dash.models.DashboardEntry`` objects.
        :return list:
        """
        entries = {}

        if not dashboard_entries:
            return entries

        for dashboard_entry in dashboard_entries:
            if dashboard_entry.placeholder_uid not in entries:
                entries[dashboard_entry.placeholder_uid] = []
            entries[dashboard_entry.placeholder_uid].append(dashboard_entry)

        return entries

    def get_placeholder_instances(self, dashboard_entries=None,
                                  workspace=None, request=None):
        """Get placeholder instances.

        :param iterable dashboard_entries: Iterable of
            ``dash.models.DashboardEntry`` objects.
        :param str workspace:
        :param django.http.HttpRequest request:
        :return list: List of `dash.base.BaseDashboardPlaceholder` subclassed
            instances.
        """
        entries = self.get_grouped_dashboard_entries(dashboard_entries)

        placeholder_instances = []

        for placeholder_cls in self.get_placeholders(request):

            placeholder = placeholder_cls(self)
            placeholder.request = request
            placeholder.workspace = workspace
            if entries:
                placeholder.dashboard_entries = entries.get(
                    placeholder_cls.uid, None
                )

            placeholder_instances.append(placeholder)

        return placeholder_instances

    @property
    def primary_html_class(self):
        return 'layout-{0}'.format(self.uid)

    @property
    def html_class(self):
        """
        Class used in the HTML.

        :return string:
        """
        return '{0} {1}'.format(self.primary_html_class,
                                ' '.join(self.html_classes))

    def get_css(self, placeholders):
        """Get placeholder specific css.

        :param iterable placeholders: Iterable of
            ``dash.base.BaseDashboardPlaceholder`` subclassed instances.
        :return string:
        """
        css = []
        for placeholder in placeholders:
            css.append(placeholder.css)
        return '\n'.join(css)

    def render_for_view(self, dashboard_entries=None, workspace=None,
                        request=None):
        """Render the layout.

        NOTE: This is not used at the moment. You most likely want the
        ``dash.views.dashboard`` view.

        :param iterable dashboard_entries:
        :param string workspace: Current workspace.
        :param django.http.HttpRequest request:
        :return string:
        """
        placeholders = self.get_placeholder_instances(
            dashboard_entries, workspace, request
        )
        context = {
            'placeholders': placeholders,
            'placeholders_dict': iterable_to_dict(
                placeholders,
                key_attr_name='uid'
            ),
            'request': request,
            'css': self.get_css(placeholders)
        }
        return render_to_string(self.get_view_template_name(request), context)

    def render_for_edit(self, dashboard_entries=None, workspace=None,
                        request=None):
        """Render the layout.

        NOTE: This is not used at the moment. You most likely want the
        ``dash.views.edit_dashboard`` view.

        :param iterable dashboard_entries:
        :param string workspace: Current workspace.
        :param django.http.HttpRequest request:
        :return string:
        """
        placeholders = self.get_placeholder_instances(
            dashboard_entries, workspace, request
        )
        context = {
            'placeholders': placeholders,
            'placeholders_dict': iterable_to_dict(
                placeholders,
                key_attr_name='uid'
            ),
            'request': request,
            'css':  self.get_css(placeholders)
        }
        return render_to_string(self.get_edit_template_name(request), context)


class BaseDashboardPlaceholder:
    """Base placeholder.

    :Properties:
        - `uid` (string): Unique identifier (shouldn't repeat within a single
          layout).
        - `cols` (int): Number of cols in the placeholder.
        - `rows` (int): Number of rows in the placeholder.
        - `cell_width` (int): Single cell (1x1) width.
        - `cell_height` (int): Single cell (1x1) height.
        - `cell_margin_top` (int): Top margin of a single cell.
        - `cell_margin_right` (int): Right margin of a single cell.
        - `cell_margin_bottom` (int): Bottom margin of a single cell.
        - `cell_margin_left` (int): Left margin of a single cell.
        - `view_template_name` (string): Template to be used for rendering the
          placeholder in view mode.
        - `edit_template_name` (string): Template to be used for rendering the
          placeholder in edit mode.
        - `html_classes` (string): Extra HTML class that layout should get.
    """

    uid = None
    cols = None  # 1
    rows = None  # 8
    cell_width = None  # 100
    cell_height = None  # 100
    cell_margin_top = 0
    cell_margin_right = 0
    cell_margin_bottom = 0
    cell_margin_left = 0
    view_template_name = ''
    edit_template_name = ''
    html_classes = []

    def __init__(self, layout):
        assert self.uid
        assert self.rows
        assert self.cols
        assert self.cell_width
        assert self.cell_height

        self.layout = layout
        self.dashboard_entries = None
        self.request = None
        self.workspace = None

    @property
    def cell_units(self):
        """Cell units."""
        return self.layout.cell_units

    @property
    def html_id(self):
        """ID (unique) used in the HTML.

        :return string:
        """
        return 'id_{0}'.format(self.uid)

    @property
    def primary_html_class(self):
        """Primary HTML class."""
        return 'placeholder-{0}'.format(self.uid)

    @property
    def html_class(self):
        """Class used in the HTML.

        :return string:
        """
        return '{0} {1}'.format(self.primary_html_class,
                                ' '.join(self.html_classes))

    def get_view_template_name(self):
        return self.view_template_name \
            if self.view_template_name \
            else DEFAULT_PLACEHOLDER_VIEW_TEMPLATE_NAME

    def get_edit_template_name(self):
        return self.edit_template_name \
            if self.edit_template_name \
            else DEFAULT_PLACEHOLDER_EDIT_TEMPLATE_NAME

    def load_dashboard_entries(self, dashboard_entries=None):
        """Feed the dashboard entries to the layout for rendering later.

        :param iterable dashboard_entries: Iterable of
            ``dash.models.DashboardEntry`` objects.
        """
        self.dashboard_entries = dashboard_entries

    def render_for_view(self):
        """Render the placeholder for view mode.

        :return string:
        """
        context = {
            'placeholder': self,
            'dashboard_entries': self.dashboard_entries,
            'request': self.request,
            'workspace': self.workspace,
        }
        return render_to_string(self.get_view_template_name(), context)

    def _generate_widget_cells(self):
        """Generates widget cells.

        Return a list of tuples, where the first element represents the cell
        class and the second element represents the cell position.

        :return list:
        """
        empty_cells = []
        position = 1
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                empty_cells.append(
                    ('col-{0} row-{1}'.format(col, row), position)
                )
                position += 1
        return empty_cells

    def render_for_edit(self):
        """Render the placeholder for edit mode.

        :return string:
        """
        context = {
            'placeholder': self,
            'dashboard_entries': self.dashboard_entries,
            'request': self.request,
            'workspace': self.workspace,
            'widget_cells': self._generate_widget_cells()
        }
        return render_to_string(self.get_edit_template_name(), context)

    def get_cell_width(self):
        """Get a single cell width, with respect to margins.

        :return int:
        """
        return self.cell_margin_left + \
            self.cell_margin_right + \
            self.cell_width

    def get_cell_height(self):
        """Get a single cell height, with respect to margins.

        :return int:
        """
        return self.cell_margin_top + \
            self.cell_margin_bottom + \
            self.cell_height

    def widget_inner_width(self, cols):
        """The inner width of the widget to be rendered."""
        return (
            (self.get_cell_width() * cols) -
            self.cell_margin_left -
            self.cell_margin_right
        )

    def widget_inner_height(self, rows):
        """The inner height of the widget to be rendered.

        :return int:
        """
        return (
            (self.get_cell_height() * rows) -
            self.cell_margin_top -
            self.cell_margin_bottom
        )

    @property
    def css(self):
        """CSS styles for the placeholders and plugins.

        The placeholder dimensions as well as columns sizes, should be
        handled here. Since we are in a placeholder and a placeholder has a
        defined number of rows and columns and each render has just a fixed
        amount of rows and columns defined, we can render the top left
        corners generic css classes.

        Cells do NOT have margins or paddings. This is essential (since all
        the plugins are positioned absolutely). If you want to have padding in
        your plugin widget, specify the `plugin-content-wrapper` class style
        in your specific layout/theme.

        :example:

            .placeholder .plugin .plugin-content-wrapper {
                padding: 5px;
            }

        :return string:
        """
        def placeholder_width():
            """Placeholder width.

            :return string:
            """
            return '{0}{1}'.format(self.cols * self.get_cell_width(),
                                   self.cell_units)

        def placeholder_height():
            """Placeholder height.

            :return string:
            """
            return '{0}{1}'.format(self.rows * self.get_cell_height(),
                                   self.cell_units)

        def plugin_width():
            """Default width of a plugin widget (1 cell).

            :return string:
            """
            return '{0}{1}'.format(self.cell_width, self.cell_units)

        def plugin_height():
            """Default height of a plugin widget (1 cell).

            :return string:
            """
            return '{0}{1}'.format(self.cell_height, self.cell_units)

        def plugin_positions():
            """Plugin positions depending on the row and cell occupied.

            All plugins are positioned absolutely. Based on the row, we use
            `margin-top` and `margin-left` to position a plugin.

            ..:Used CSS classes:
                - `row-1`, `row-2`, etc.
                - `col-1`, `col-2`, etc.

            :return string:
            """
            positions = []
            row_template = """
            .placeholder.{placeholder_class} .empty-widget-cell.row-{row_num},
            .placeholder.{placeholder_class} .plugin.row-{row_num} {{
                margin-top: {top};
            }}
            """
            for row_num in range(0, self.rows):
                _val = row_template.format(
                    placeholder_class=self.primary_html_class,
                    row_num=(row_num + 1),
                    top='{0}{1}'.format(self.get_cell_height() * row_num,
                                        self.cell_units)
                )
                positions.append(_val)

            col_template = """
            .placeholder.{placeholder_class} .empty-widget-cell.col-{col_num},
            .placeholder.{placeholder_class} .plugin.col-{col_num} {{
                margin-left: {left};
            }}
            """
            for col_num in range(0, self.cols):
                _val = col_template.format(
                    placeholder_class=self.primary_html_class,
                    col_num=(col_num + 1),
                    left='{0}{1}'.format(self.get_cell_width() * col_num,
                                         self.cell_units)
                )
                positions.append(_val)

            return '\n'.join(positions)

        def plugin_sizes():
            """Plugin size based on its' `rows` and `cols` properties.

            ..:Used CSS classes:
                - `width-1`, `width-2`, etc.
                - `height-1`, `height-2`, etc.

            :return string:
            """
            sizes = []

            row_template = """
            .placeholder.{placeholder_class} .plugin.height-{row_num} {{
                height: {height};
            }}
            """
            for row_num in range(0, self.rows):
                _val = row_template.format(
                    placeholder_class=self.primary_html_class,
                    row_num=(row_num + 1),
                    height='{0}{1}'.format(
                        self.widget_inner_height(row_num + 1),
                        self.cell_units
                    )
                )
                sizes.append(_val)

            col_template = """
            .placeholder.{placeholder_class} .plugin.width-{col_num} {{
                width: {width};
            }}
            """
            for col_num in range(0, self.cols):
                _val = col_template.format(
                    placeholder_class=self.primary_html_class,
                    col_num=(col_num + 1),
                    width='{0}{1}'.format(
                        self.widget_inner_width(col_num + 1),
                        self.cell_units
                    )
                )
                sizes.append(_val)

            return '\n'.join(sizes)

        def empty_cell_size():
            """CSS for empty cell size."""
            _val = """
            .placeholder.{placeholder_class} .empty-widget-cell {{
                width: {width};
                height: {height};
                line-height: {height};
            }}
            """.format(
                placeholder_class=self.primary_html_class,
                width='{0}{1}'.format(self.cell_width, self.cell_units),
                height='{0}{1}'.format(self.cell_height, self.cell_units)
            )
            return _val

        css = """
        .placeholder.{placeholder_class} {{
            width: {placeholder_width};
            height: {placeholder_height};
        }}

        .placeholder.{placeholder_class} .plugin {{
            width: {plugin_width};
            height: {plugin_height};
        }}

        {plugin_positions}

        {plugin_sizes}

        {empty_cell_sizes}
        """.format(
            placeholder_class=self.primary_html_class,
            placeholder_width=placeholder_width(),
            placeholder_height=placeholder_height(),
            plugin_width=plugin_width(),
            plugin_height=plugin_height(),
            plugin_positions=plugin_positions(),
            plugin_sizes=plugin_sizes(),
            empty_cell_sizes=empty_cell_size()
        )

        return css


class DashboardPluginDataStorage:
    """Storage for plugin data."""


class BaseDashboardPlugin:
    """Base dashboard plugin from which every plugin should inherit.

    :Properties:
        - `uid` (string): Plugin uid (obligatory). Example value: 'dummy',
          'wysiwyg', 'news'.
        - `name` (string): Plugin name (obligatory). Example value:
          'Dummy plugin', 'WYSIWYG', 'Latest news'.
        - `description` (string): Plugin description (optional). Example
          value: 'Dummy plugin used just for testing'.
        - `help_text` (string): Plugin help text (optional). This text would
          be shown in ``dash.views.add_dashboard_entry``.
          and ``dash.views.edit_dashboard_entry`` views.
        - `form`: Plugin form (optional). A subclass of ``django.forms.Form``.
          Should be given in case plugin is configurable.
        - `add_form_template` (str) (optional): Add form template (optional).
          If given, overrides the ``dash.views.add_dashboard_entry`` default
          template.
        - `edit_form_template` (string): Edit form template (optional). If
          given, overrides the ``dash.views.edit_dashboard_entry`` default
          template.
        - `html_classes` (list): List of extra HTML classes for the plugin.
        - `group` (string): Plugin are grouped under the specified group.
          Override in your plugin if necessary.
    """
    uid = None
    name = None
    description = None
    help_text = None
    form = None
    add_form_template = None
    edit_form_template = None
    html_classes = []
    group = _("General")

    def __init__(self, layout_uid, placeholder_uid, workspace=None,
                 user=None, position=None):
        """
        :param string placeholder_uid: Unique identifier of plugin
            placeholder (layout.placeholder).
        :param dash.models.DashboardWorkspace workspace: Plugin workspace.
        :param django.contrib.auth.models.User user: Plugin owner.
        """
        # Making sure all necessary properties are defined.
        try:
            assert self.uid
            assert self.name
        except Exception as e:
            raise NotImplementedError(
                "You should define `uid` and `name` properties in your "
                "`{0}.{1}` class.".format(self.__class__.__module__,
                                          self.__class__.__name__)
            )

        layout_cls = layout_registry.get(layout_uid, None)
        self.layout = layout_cls() if layout_cls else None

        placeholder_cls = self.layout.get_placeholder(placeholder_uid)
        self.placeholder = placeholder_cls(self.layout) \
            if placeholder_cls \
            else None

        if not (self.layout and self.placeholder):
            raise Exception(
                "Invalid placeholder value {0} in "
                "your `{1}.{2}` class.".format(
                    placeholder_uid,
                    self.__class__.__module__,
                    self.__class__.__name__
                )
            )

        self.layout_uid = layout_uid
        self.placeholder_uid = placeholder_uid
        self.workspace = workspace
        self.user = user
        self.position = position

        # Some initial values
        self.request = None

        self.data = DashboardPluginDataStorage()

        self._html_id = 'p{0}'.format(uuid.uuid4())

    @property
    def html_id(self):
        """HTML id."""
        return self._html_id

    def get_position(self):
        """Get the exact position of the plugin widget in the placeholder (row
        number, col number).

        :return tuple: Tuple of row and col numbers.
        """
        col = self.position % self.placeholder.cols
        row = int(
            self.position / self.placeholder.cols
        ) + (1 if col > 0 else 0)
        if col == 0:
            col = self.placeholder.cols

        return row, col

    @property  # Comment the @property out if something goes wrong.
    def html_class(self):
        """HTML class.

        A massive work on positioning the plugin and having it to be displayed
        in a given width is done here. We should be getting the plugin widget
        for the plugin given and based on its' properties (static!) as well as
        on plugin position (which we have from model), we can show the plugin
        with the exact class.
        """
        try:
            widget = self.get_widget()
            row, col = self.get_position()
            html_class = [
                'plugin-{0} {1} {2}'.format(
                    self.uid,
                    widget.html_class,
                    ' '.join(self.html_classes)
                ),
                'width-{0}'.format(widget.cols),
                'height-{0}'.format(widget.rows),
                'row-{0}'.format(row),
                'col-{0}'.format(col),
            ]

            return ' '.join(html_class)
        except Exception as err:
            logger.debug(str(err))

    def process(self, plugin_data=None, fetch_related_data=False):
        """Init plugin with data."""
        try:
            # Calling pre-processor.
            self.pre_processor()

            if plugin_data:
                try:
                    # Trying to load the plugin data to JSON.
                    plugin_data = json.loads(plugin_data)

                    # If a valid JSON object, feed it to our plugin and
                    # process the data. The ``process_data`` method should
                    # be defined in your subclassed plugin class.
                    if plugin_data:
                        self.load_plugin_data(plugin_data)

                        self.process_plugin_data(
                            fetch_related_data=fetch_related_data
                        )
                except Exception as err:
                    if DEBUG:
                        logger.debug(str(err))

            # Calling the post processor.
            self.post_processor()

            return self
        except Exception as err:
            if DEBUG:
                logger.debug(str(err))

    def load_plugin_data(self, plugin_data):
        """Load the plugin data saved in ``dash.models.DashboardEntry``.
        Plugin data is saved in JSON string.

        :param string plugin_data: JSON string with plugin data.
        """
        self.plugin_data = plugin_data

    def _process_plugin_data(self, fields, fetch_related_data=False):
        """Process the plugin data.

        Override if need customisations.

        Beware, this is not always called.
        """
        for field, default_value in fields:
            try:
                setattr(
                    self.data,
                    field,
                    self.plugin_data.get(field, default_value)
                )
            except Exception:
                setattr(self.data, field, default_value)

    def process_plugin_data(self, fetch_related_data=False):
        """Processes the plugin data."""
        form = self.get_form()

        return self._process_plugin_data(
            form.plugin_data_fields,
            fetch_related_data=fetch_related_data
        )

    def _get_plugin_form_data(self, fields):
        """Get plugin data.

        :param iterable fields: List of tuples to iterate.
        :return dict:
        """
        form_data = {}
        for field, default_value in fields:
            try:
                form_data.update(
                    {field: self.plugin_data.get(field, default_value)}
                )
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
        return form_data

    def get_plugin_form_data(self):
        """Get plugin form data.

        Fed as ``initial`` argument to the plugin form when initialising the
        instance for adding or editing the plugin. Override in your plugin
        class if you need customisations.
        """
        form = self.get_form()

        return self._get_plugin_form_data(form.plugin_data_fields)

    def get_instance(self):
        """Get instances."""
        return None

    def get_form(self):
        """Get the plugin form class.

        Override this method in your subclassed ``dash.base.DashboardPlugin``
        class when you need your plugin setup to vary depending on the
        placeholder, workspace, user or request given. By default returns the
        value of the ``form`` attribute defined in your plugin.

        :return django.forms.Form|django.forms.ModelForm: Subclass of
            ``django.forms.Form`` or ``django.forms.ModelForm``.
        """
        return self.form

    def get_initialised_create_form(self, data=None, files=None):
        """
        Used ``dash.views.add_dashboard_entry`` view to gets initialised form
        for object to be created.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                plugin_form = self.get_form()
                if plugin_form:
                    return plugin_form(data=data, files=files)
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
                raise Http404(err)

    def get_initialised_create_form_or_404(self, data=None, files=None):
        """Get initialised create form or 404.

        Same as ``get_initialised_create_form`` but raises
        ``django.http.Http404`` on errors.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                return self.get_initialised_create_form(data=data, files=files)
            except Exception as e:
                if DEBUG:
                    logger.debug(e)
                raise Http404(e)

    def get_initialised_edit_form(self, data=None, files=None,
                                  auto_id='id_%s', prefix=None, initial=None,
                                  error_class=ErrorList, label_suffix=':',
                                  empty_permitted=False, instance=None):
        """Get initialised edit form.

        Used in ``dash.views.edit_dashboard_entry`` view.
        """
        plugin_form = self.get_form()
        if plugin_form:
            kwargs = {
                'data': data,
                'files': files,
                'auto_id': auto_id,
                'prefix': prefix,
                'initial': initial,
                'error_class': error_class,
                'label_suffix': label_suffix,
                'empty_permitted': empty_permitted
            }
            if issubclass(plugin_form, ModelForm):
                kwargs.update({'instance': instance})
            return plugin_form(**kwargs)

    def get_initialised_edit_form_or_404(self, data=None, files=None,
                                         auto_id='id_%s', prefix=None,
                                         error_class=ErrorList,
                                         label_suffix=':',
                                         empty_permitted=False):
        """Get initialised edit form or 404.

        Same as ``get_initialised_edit_form`` but raises
        ``django.http.Http404`` on errors.
        """
        plugin_form = self.get_form()
        if plugin_form:
            try:
                return self.get_initialised_edit_form(
                    data=data,
                    files=files,
                    auto_id=auto_id,
                    prefix=prefix,
                    initial=self.get_plugin_form_data(),
                    error_class=error_class,
                    label_suffix=label_suffix,
                    empty_permitted=empty_permitted,
                    instance=self.get_instance()
                )
            except Exception as err:
                if DEBUG:
                    logger.debug(err)
                raise Http404(err)

    def get_widget(self, request=None, as_instance=False):
        """Get the plugin widget.

        :param django.http.HttpRequest request:
        :param bool as_instance:
        :return mixed: Subclass of ``dash.base.BaseDashboardPluginWidget`` or
            instance of subclassed ``dash.base.BaseDashboardPluginWidget``
            object.
        """
        widget_cls = plugin_widget_registry.get(
            PluginWidgetRegistry.namify(self.layout.uid,
                                        self.placeholder.uid,
                                        self.uid)
            )

        if not as_instance:
            return widget_cls
        elif widget_cls:
            widget = widget_cls(self)
            return widget

    def render(self, request=None):
        """Render the plugin HTML (for dashboard workspace).

        :param django.http.HttpRequest request:
        :return string:
        """
        widget_cls = self.get_widget()

        if widget_cls:
            widget = widget_cls(self)

            render = widget.render(request=request)
            return render or ''
        elif DEBUG:
            logger.debug(
                "No widget defined for {0}.{1}.{2}".format(
                    self.layout.uid,
                    self.placeholder.uid,
                    self.uid
                )
            )

    def _update_plugin_data(self, dashboard_entry):
        """Update plugin data.

        For private use. Do not override this method. Override
        ``update_plugin_data`` instead.
        """
        try:
            updated_plugin_data = self.update_plugin_data(dashboard_entry)
            plugin_data = self.get_updated_plugin_data(
                update=updated_plugin_data
            )
            return self.save_plugin_data(
                dashboard_entry,
                plugin_data=plugin_data
            )
        except Exception as err:
            logging.debug(str(err))

    def update_plugin_data(self, dashboard_entry):
        """Update plugin data.

        Used in ``dash.management.commands.dash_update_plugin_data``.

        Some plugins would contain data fetched from various sources (models,
        remote data). Since dashboard entries are by definition loaded
        extremely much, you are advised to store as much data as possible in
        ``plugin_data`` field of ``dash.models.DashboardEntry``. Some
        externally fetched data becomes invalid after some time and needs
        updating. For that purpose, in case if your plugin needs that, redefine
        this method in your plugin. If you need your data to be periodically
        updated, add a cron-job which would run ``dash_update_plugin_data``
        management command (see
        ``dash.management.commands.dash_update_plugin_data`` module).

        :param dash.models.DashboardEntry dashboard_entry: Instance of
            ``dash.models.DashboardEntry``.
        :return dict: Should return a dictionary containing data of fields to
            be updated.
        """

    def _delete_plugin_data(self):
        """
        For private use. Do not override this method. Override
        ``delete_plugin_data`` instead.
        """
        try:
            self.delete_plugin_data()
        except Exception as e:
            logging.debug(str(e))

    def delete_plugin_data(self):
        """Delete plugin data.

        Used in ``dash.views.delete_dashboard_entry``. Fired automatically,
        when ``dash.models.DashboardEntry`` object is about to be deleted. Make
        use of it if your plugin creates database records or files that are
        not monitored externally but by dash only.
        """

    def _clone_plugin_data(self, dashboard_entry):
        """Clone plugin data.

        For private use. Do not override this method. Override
        ``clone_plugin_data`` instead.
        """
        try:
            return self.clone_plugin_data(dashboard_entry)
        except Exception as err:
            logging.debug(str(err))

    def clone_plugin_data(self, dashboard_entry):
        """Clone plugin data.

        Used when copying entries. If any objects or files are created by
        plugin, they should be cloned.

        :param dash.models.DashboardEntry dashboard_entry: Instance of
            ``dash.models.DashboardEntry``.
        :return string: JSON dumped string of the cloned plugin data. The
            returned value would be inserted as is into the
            ``dash.models.DashboardEntry.plugin_data`` field.
        """

    def get_cloned_plugin_data(self, update={}):
        """Get the cloned plugin data and returns it in a JSON dumped format.

        :param dict update:
        :return string: JSON dumped string of the cloned plugin data.

        :example:

        In the ``get_cloned_plugin_data`` method of your plugin, do as follows:

        >>> def clone_plugin_data(self, dashboard_entry):
        >>>     cloned_image = clone_file(self.data.image, relative_path=True)
        >>>     return self.get_cloned_plugin_data(
        >>>         update={'image': cloned_image}
        >>>     )
        """
        form = self.get_form()

        cloned_data = copy.copy(self.data)
        data = {}

        for field, default_value in form.plugin_data_fields:
            data.update({field: getattr(cloned_data, field, '')})

        for prop, value in update.items():
            data.update({prop: value})

        return json.dumps(data)

    def get_updated_plugin_data(self, update={}):
        """Get the plugin data and returns it in a JSON dumped format.

        :param dict update:
        :return string: JSON dumped string of the cloned plugin data.
        """
        form = self.get_form()
        data = {}

        for field, default_value in form.plugin_data_fields:
            data.update({field: getattr(self.data, field, '')})

        for prop, value in update.items():
            data.update({prop: value})

        return json.dumps(data)

    def pre_processor(self):
        """Pre-process data.

        Redefine in your subclassed plugin when necessary.

        Pre process plugin data (before rendering). This method is being
        called before the data has been loaded into the plugin.

        Note, that request (django.http.HttpRequest) is
        available (self.request).
        """

    def post_processor(self):
        """Post-process data.

        Redefine in your subclassed plugin when necessary.

        Post process plugin data here (before rendering). This method is being
        called after the data has been loaded into the plugin.

        Note, that request (django.http.HttpRequest) is
        available (self.request).
        """

    def save_plugin_data(self, dashboard_entry, plugin_data):
        """Save plugin data.

        Used in bulk update plugin data.

        :param dash.models.DashboardEntry dashboard_entry:
        :param dict plugin_data:
        :return bool: True if all went well.
        """
        try:
            if plugin_data:
                dashboard_entry.plugin_data = plugin_data
                dashboard_entry.save()
                return True
        except Exception as err:
            logger.debug(str(err))


class MetaBaseDashboardPluginWidget(type):
    """Meta class for ``dash.base.BaseDashboardPluginWidget``."""

    @property
    def html_class(cls):
        """HTML class of the ``dash.base.BaseDashboardPluginWidget``.

        :return string:
        """
        return ' '.join(cls.html_classes)


class ClassProperty(property):
    """Class property."""
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


classproperty = ClassProperty


class BaseDashboardPluginWidget:
    """Base plugin widget.

    So, if we would want to register a plugin widget (renderer) for some
    layout, we would first define the plugin widget and then just write:

        >>> plugin_widget_registry.register(DummyPluginWidget)

    Plugin widget is always being registered for a placeholder. Placeholder in
    its' turn has number of rows and columns. Since we register each widget
    for a (layout, placeholder, plugin) combination separately, it fits the
    needs and requirements perfectly. In that way we are able to tell, whether
    plugin has a widget available and actually valid (qua dimensions) for the
    placeholder. Plugin is just data. Nothing more. Widget operates with that
    data. Thus, widget has number of rows and columns it occupies in the
    placeholder registered. By default, number of rows and columns is set to
    1, which means that a plugin occupies just 1 cell. But, certainly, there
    can be plugins that occupy more space in a placeholder.
    """

    layout_uid = None
    placeholder_uid = None
    plugin_uid = None
    cols = 1
    rows = 1
    html_classes = []
    media_js = []
    media_css = []

    def __init__(self, plugin):
        assert self.layout_uid and self.layout_uid == plugin.layout.uid
        assert (
            self.placeholder_uid
            and
            self.placeholder_uid in plugin.layout.placeholder_uids
        )
        assert (
            self.plugin_uid
            and
            self.plugin_uid in get_registered_plugin_uids()
        )
        assert hasattr(self, 'render') and callable(self.render)
        assert self.cols
        assert self.rows
        assert isinstance(self.media_js, (list, tuple))
        assert isinstance(self.media_css, (list, tuple))

        if isinstance(self.media_js, tuple):
            self.media_js = list(self.media_js)

        if isinstance(self.media_css, tuple):
            self.media_css = list(self.media_css)

        self.plugin = plugin

    def render(self, request=None):
        """Render.

        :param django.http.HttpRequest request:
        :return str:
        """
        return ''

    @classproperty
    def html_class(cls):
        """HTML class of the ``dash.base.BaseDashboardPluginWidget``.

        :return string:
        """
        return ' '.join(cls.html_classes)

    def get_width(self):
        """Get widget width.

        :return int:
        """
        return self.plugin.placeholder.widget_inner_width(self.cols)

    def get_height(self):
        """Get widget height.

        :return int:
        """
        return self.plugin.placeholder.widget_inner_height(self.rows)

    def get_size(self, delta_width=0, delta_height=0):
        """Get widget size.

        :param int delta_width:
        :param int delta_height:
        :return tuple:
        """
        return (
            (
                self.cols * self.plugin.placeholder.get_cell_width()
            ) + delta_width,
            (
                self.rows * self.plugin.placeholder.get_cell_height()
            ) + delta_height
        )


class BaseRegistry:
    """Registry of dash plugins.

    It's essential, that class registered has the``uid`` property.
    """

    type = None

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    def register(self, cls, force=False):
        """
        Registers the plugin in the registry.

        :param cls mixed.
        :param bool force:
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for "
                "registry `{1}`".format(cls, self.__class__)
            )

        # If item has not been forced yet, add/replace its' value in the
        # registry
        if force:

            if cls.uid not in self._forced:
                self._registry[cls.uid] = cls
                self._forced.append(cls.uid)
                return True
            else:
                return False

        else:

            if cls.uid in self._registry:
                return False
            else:
                self._registry[cls.uid] = cls
                return True

    def unregister(self, cls):
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for "
                "registry `{1}`".format(cls, self.__class__)
            )

        # Only non-forced items are allowed to be unregistered.
        if cls.uid in self._registry and cls.uid not in self._forced:
            self._registry.pop(cls.uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """Get the given entry from the registry.

        :param string uid:
        :param mixed default:
        :return mixed.
        """
        item = self._registry.get(uid, default)
        if not item:
            logger.debug(
                "Can't find plugin with uid `{0}` in `{1}` "
                "registry".format(uid, self.__class__)
            )
        return item


class PluginRegistry(BaseRegistry):
    """Plugin registry."""

    type = BaseDashboardPlugin


class LayoutRegistry(BaseRegistry):
    """Layout registry."""

    type = BaseDashboardLayout


class PluginWidgetRegistry:
    """Registry of dash plugins widgets (renderers)."""

    type = BaseDashboardPluginWidget

    def __init__(self):
        assert self.type
        self._registry = {}
        self._forced = []

    @staticmethod
    def namify(layout, placeholder, plugin_uid):
        return '{0}.{1}.{2}'.format(layout, placeholder, plugin_uid)

    def register(self, cls, force=False):
        """Register the plugin renderer in the registry.

        :param dash.base.BasePluginRenderer cls: Subclass of
            ``dash.base.BasePluginRenderer``.
        """
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for "
                "registry `{1}`".format(cls, self.__class__)
            )

        uid = PluginWidgetRegistry.namify(
            cls.layout_uid,
            cls.placeholder_uid,
            cls.plugin_uid
        )

        # If item has not been forced yet, add/replace its' value in the
        # registry.
        if force:

            if uid not in self._forced:
                self._registry[uid] = cls
                self._forced.append(uid)
                return True
            else:
                return False

        else:

            if uid in self._registry:
                return False
            else:
                self._registry[uid] = cls
                return True

    def unregister(self, cls):
        if not issubclass(cls, self.type):
            raise InvalidRegistryItemType(
                "Invalid item type `{0}` for "
                "registry `{1}`".format(cls, self.__class__)
            )

        uid = PluginWidgetRegistry.namify(
            cls.layout_uid,
            cls.placeholder_uid,
            cls.plugin_uid
        )

        # Only non-forced items are allowed to be unregistered.
        if uid in self._registry and uid not in self._forced:
            self._registry.pop(uid)
            return True
        else:
            return False

    def get(self, uid, default=None):
        """Get the given entry from the registry.

        :param string uid:
        :param mixed default:
        :return mixed.
        """
        item = self._registry.get(uid, default)
        if not item:
            logger.debug(
                "Can't find plugin with uid `{0}` in `{1}` "
                "registry".format(uid, self.__class__)
            )
        return item


# Register plugins by calling plugin_registry.register()
plugin_registry = PluginRegistry()

# Register layouts by calling layout_registry.register()
layout_registry = LayoutRegistry()

# Register of plugin widgets.
plugin_widget_registry = PluginWidgetRegistry()


def ensure_autodiscover():
    """Ensure that plugins are auto-discovered."""
    if not (
        plugin_registry._registry and
        layout_registry._registry and
        plugin_widget_registry._registry
    ):
        autodiscover()


def get_registered_plugins():
    """Get a list of registered plugins in a form if tuple.

    Get a list of registered plugins in a form if tuple (plugin name, plugin
    description). If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    ensure_autodiscover()

    registered_plugins = []

    for uid, plugin in plugin_registry._registry.items():
        registered_plugins.append((uid, safe_text(plugin.name)))

    return registered_plugins


def get_registered_plugin_uids():
    """Gets a list of registered plugin uids as a list .

    If not yet auto-discovered, auto-discovers them.

    :return list:
    """
    ensure_autodiscover()

    registered_plugins = []

    for uid, plugin in plugin_registry._registry.items():
        registered_plugins.append(uid)
    return registered_plugins


def validate_placeholder_uid(layout, placeholder_uid):
    """Validate the placeholder.

    :param string layout:
    :param string placeholder_uid:
    :return bool:
    """
    return placeholder_uid in layout.placeholder_uids


def validate_plugin_uid(plugin_uid):
    """Validate the plugin uid.

    :param string plugin_uid:
    :return bool:
    """
    return plugin_uid in get_registered_plugin_uids()


def get_registered_layouts():
    """Get registered layouts."""
    ensure_autodiscover()

    registered_layouts = []

    for uid, layout in layout_registry._registry.items():
        registered_layouts.append((uid, safe_text(layout.name)))

    return registered_layouts


def get_registered_layout_uids():
    """Get uids of registered layouts."""
    return layout_registry._registry.keys()


def get_layout(layout_uid=None, as_instance=False):
    """Gets the layout by ``layout_uid`` given.

    If left empty, takes the default one chosen in settings.

    Raises a ``dash.exceptions.NoActiveLayoutChosen`` when no default layout
    could be found.

    :return dash.base.BaseDashboardLayout: Sublcass of
        ``dash.base.BaseDashboardLayout``.
    """
    ensure_autodiscover()

    if not layout_uid:
        layout_uid = ACTIVE_LAYOUT

    layout_cls = layout_registry.get(layout_uid, None)
    if not layout_cls:
        raise LayoutDoesNotExist(
            _("Layout `{0}` does not exist!").format(layout_uid)
        )

    if as_instance:
        return layout_cls()

    return layout_cls


def collect_widget_media(dashboard_entries):
    """Collect the widget media for dashboard entries given.

    :param iterable dashboard_entries: Iterable of
        ``dash.models.DashboardEntry`` instances.
    :return dict: Returns a dict containing the 'js' and 'css' keys.
        Correspondent values of those keys are lists containing paths to the
        CSS and JS media files.
    """
    media_js = []
    media_css = []
    for dashboard_entry in dashboard_entries:
        widget_cls = plugin_widget_registry.get(
            PluginWidgetRegistry.namify(
                dashboard_entry.layout_uid,
                dashboard_entry.placeholder_uid,
                dashboard_entry.plugin_uid
            )
        )
        if widget_cls:
            media_js += widget_cls.media_js
            media_css += widget_cls.media_css
        else:
            logger.debug(
                "widget_cls empty for dashboard "
                "entry {0}".format(dashboard_entry.__dict__)
            )
    return {'js': media_js, 'css': media_css}
