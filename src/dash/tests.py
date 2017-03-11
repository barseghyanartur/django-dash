# from optparse import OptionParser
from time import sleep
import unittest

from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.staticfiles.management.commands import collectstatic
from django.core.management import call_command
from django.test import (
    TestCase,
    RequestFactory,
    LiveServerTestCase,
    # Client,
)

from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from six import print_

from .base import (
    get_layout,
    get_registered_layouts,
    # get_registered_plugins,
    # layout_registry,
    # plugin_registry,
)
# from .discover import autodiscover
# from .management.commands import dash_sync_plugins
from .models import DashboardEntry
from .settings import WAIT_BETWEEN_TEST_STEPS, WAIT_AT_TEST_END
from .utils import get_occupied_cells, get_user_plugins

__title__ = 'dash.tests'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'


DASH_TEST_USER_USERNAME = 'test_admin'
DASH_TEST_USER_PASSWORD = 'test'
PRINT_INFO = True
TRACK_TIME = False


def print_info(func):
    """Prints some useful info."""
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print_('\n{0}'.format(func.__name__))
        print_('============================')
        if func.__doc__:
            print_('""" {0} """'.format(func.__doc__.strip()))
        print_('----------------------------')
        if result is not None:
            print_(result)
        print_('\n')

        return result
    return inner


def create_dashboard_user():
    """
    Create a user for testing the dashboard.

    TODO: At the moment an admin account is being tested. Automated tests with
    diverse accounts are to be implemented.
    """
    User = get_user_model()
    u = User()
    u.username = DASH_TEST_USER_USERNAME
    u.email = 'admin@dev.django-dash.com'
    u.is_superuser = True
    u.is_staff = True
    u.set_password(DASH_TEST_USER_PASSWORD)

    try:
        u.save()
    except Exception as err:
        pass


DASH_SET_UP = False


def setup_dash():
    """Set up dash."""
    call_command('collectstatic', verbosity=3, interactive=False)
    call_command('dash_sync_plugins', verbosity=3, interactive=False)


class DashCoreTest(TestCase):
    """Tests of django-dash core functionality."""

    def setUp(self):
        setup_dash()

    @print_info
    def test_01_registered_layouts(self):
        """Test registered layouts (`get_registered_layouts`)."""
        res = get_registered_layouts()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_02_active_layout(self):
        """Test active layout (`get_layout`)."""
        layout_cls = get_layout()
        self.assertTrue(layout_cls is not None)
        return layout_cls

    @print_info
    def test_03_get_layout_placeholders(self):
        """Test active layout placeholders (`get_placeholder_instances`)."""
        layout_cls = get_layout()
        layout = layout_cls()
        res = layout.get_placeholder_instances()
        self.assertTrue(len(res) > 0)
        return res

    @print_info
    def test_04_active_layout_render_for_view(self):
        """Test active layout render (`render_for_view`)."""
        try:
            # Create dashboard user
            create_dashboard_user()
        except Exception:
            pass

        User = get_user_model()
        # Getting the admin (user with plugin data)
        user = User.objects.get(username=DASH_TEST_USER_USERNAME)

        # Faking the Django request
        request_factory = RequestFactory()
        request = request_factory.get('/dashboard/', data={'user': user})
        request.user = user
        workspace = None

        # Getting the list of plugins that user is allowed to use.
        registered_plugins = get_user_plugins(request.user)
        user_plugin_uids = [uid for uid, repr in registered_plugins]

        layout = get_layout(as_instance=True)

        # Fetching all dashboard entries for user and freezeing the queryset
        dashboard_entries = DashboardEntry \
            ._default_manager \
            .get_for_user(user=request.user,
                          layout_uid=layout.uid,
                          workspace=workspace) \
            .select_related('workspace', 'user') \
            .filter(plugin_uid__in=user_plugin_uids) \
            .order_by('placeholder_uid', 'position')[:]

        res = layout.render_for_view(dashboard_entries=dashboard_entries,
                                     request=request)
        return res

    @print_info
    def test_05_get_occupied_cells(self):
        """Test ``dash.utils.get_occupied_cells``."""
        # Fake dashboard entry
        class Entry(object):
            pass

        layout = get_layout(as_instance=True)
        placeholder = layout.get_placeholder('main')

        res = []

        if 'android' == layout.uid:
            # *********** First test
            # 2 x 2 widget
            r = get_occupied_cells(layout, placeholder, 'memo_2x2', 3)

            self.assertEqual(r, [3, 4, 9, 10])

            res.append(r)

            # *********** Second test

            # 3 x 3 widget
            r = get_occupied_cells(layout, placeholder, 'memo_3x3', 16)

            self.assertEqual(r, [16, 17, 18, 22, 23, 24, 28, 29, 30])

            res.append(r)

            # *********** Third test (the nasty one)

            # 3 x 3 widget
            # r = get_occupied_cells(layout, placeholder, 'memo_3x3', 17)

            # self.assertEqual(r, [16, 17, 18, 22, 23, 24, 28, 29, 30])

            # res.append(r)

        return res


class DashBrowserTest(LiveServerTestCase):
    """django-dash browser tests.

    TODO: At the moment is done for admin only. Normal users shall be tested
    as well for plugin security workflow (permissions system used).
    """
    try:
        LIVE_SERVER_URL = settings.LIVE_SERVER_URL
    except Exception as e:
        LIVE_SERVER_URL = None

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        # cls.selenium = WebDriver()
        firefox_bin_path = getattr(settings, 'FIREFOX_BIN_PATH', None)
        phantom_js_executable_path = getattr(
            settings, 'PHANTOM_JS_EXECUTABLE_PATH', None
        )
        if phantom_js_executable_path is not None:
            if phantom_js_executable_path:
                cls.selenium = webdriver.PhantomJS(
                    executable_path=phantom_js_executable_path
                )
            else:
                cls.selenium = webdriver.PhantomJS()
        elif firefox_bin_path:
            binary = FirefoxBinary(firefox_bin_path)
            cls.selenium = webdriver.Firefox(firefox_binary=binary)
        else:
            cls.selenium = webdriver.Firefox()

        setup_dash()

        super(DashBrowserTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        """Tear down class."""
        try:
            cls.selenium.quit()
        except Exception as err:
            print(err)

        super(DashBrowserTest, cls).tearDownClass()
        call_command('flush', verbosity=0, interactive=False,
                     reset_sequences=False,
                     allow_cascade=False,
                     inhibit_post_migrate=False)

    def _click(self, element):
        """Click on any element."""
        self.selenium.execute_script("$(arguments[0]).click();", element)

    def _agressive_click(self, element):
        """Agressive click."""
        link = element.get_attribute('href')
        self.selenium.get(link)

    def __add_plugin_widget_test(self,
                                 position,
                                 plugin_widget_name,
                                 plugin_widget_name_with_dimensions,
                                 plugin_widget_css_class,
                                 added_plugin_widget_css_classes,
                                 form_data={},
                                 form_hook_func=None):
        """
        Test add any single plugin.

        :param string position: Example value "col-1 row-1"
        :param string plugin_widget_name: Example value "Dummy".
        :param string plugin_widget_name_with_dimensions: Example
            value "Dummy (1x1)".
        :param string plugin_widget_css_class: Example value "plugin-dummy1x1".
        :param list added_plugin_widget_css_classes: Example
            value ['width-1', 'height-1'].
        :param dict form_data: Example value
            {
                'title': "Lorem",
                'text': "Lorem ipsum dolor sit amet"
            }.
        :param callable form_hook_func: Function to when add form is opened (
            to populate the data).

        :example:

        Test 1x1 URL plugin widget::

            def choose_url_image():
                # Hook function to select an image for test 1x1
                # URL plugin widget.
                image_input = self.selenium.find_element_by_xpath(
                    '//select[@name="image"]/option[@value="icon-coffee"]'
                )
                self.assertTrue(image_input is not None)
                image_input.click()


            self.__add_plugin_widget_test(
                position="col-1 row-1",
                plugin_widget_name="URL",
                plugin_widget_name_with_dimensions="URL (1x1)",
                plugin_widget_css_class="plugin-url_1x1",
                added_plugin_widget_css_classes ('width-1', 'height-1'),
                form_data={
                    'title': "Test 1x1 URL",
                    'url': "http://delusionalinsanity.com/portfolio/"
                },
                form_hook_func=choose_url_image
            )

        Test 2x1 Dummy plugin widget::

            self.__add_plugin_widget_test(
                position="col-2 row-1",
                plugin_widget_name="Dummy",
                plugin_widget_name_with_dimensions="Dummy (2x1)",
                plugin_widget_css_class="plugin-dummy2x1",
                added_plugin_widget_css_classes=('width-2', 'height-1')
            )

        Test 3x3 Memo plugin widget::

            self.__add_plugin_widget_test(
                position="col-4 row-1",
                plugin_widget_name="Memo",
                plugin_widget_name_with_dimensions="Memo (3x3)",
                plugin_widget_css_class="plugin-memo_3x3",
                added_plugin_widget_css_classes=('width-3', 'height-3'),
                form_data={
                    'title': "Lorem",
                    'text': "Lorem ipsum dolor sit amet"
                }
            )

        Test 3x3 Video plugin widget::

            self.__add_plugin_widget_test(
                position="col-1 row-2",
                plugin_widget_name="Video",
                plugin_widget_name_with_dimensions="Video (3x3)",
                plugin_widget_css_class="plugin-video_3x3",
                added_plugin_widget_css_classes=('width-3', 'height-3'),
                form_data = {
                    'title': "Test 3x3 video",
                    'url': "http://www.youtube.com/watch?v=8GVIui0JK0M"
                }
            )
        """
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 1: Dashboard user logs in ++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        live_server_url = self.LIVE_SERVER_URL \
            if self.LIVE_SERVER_URL \
            else self.live_server_url
        self.selenium.get('{0}{1}'.format(live_server_url, settings.LOGIN_URL))
        self.selenium.maximize_window()
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(DASH_TEST_USER_USERNAME)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(DASH_TEST_USER_PASSWORD)
        submit_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        submit_button.click()

        # Wait until the list view opens
        WebDriverWait(self.selenium, timeout=4).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "layout")]'
            )
        )

        # Click the button to go to dashboard edit
        dashboard_edit_link = self.selenium.find_element_by_xpath(
            '//a[contains(@class, "menu-dashboard-edit")]'
        )
        dashboard_edit_link.click()

        # Wait until the dashboard edit view opens
        WebDriverWait(self.selenium, timeout=4).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "layout")]'
            )
        )

        # Click the add widget button to add a new widget to the dashboard
        add_plugin_widget_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(position)
        )
        add_plugin_link = add_plugin_widget_div.find_element_by_class_name(
            'add-plugin'
        )
        # add_plugin_link.click()
        self._click(add_plugin_link)

        # Wait until the add widget view opens
        WebDriverWait(self.selenium, timeout=8).until(
            lambda driver: driver.find_element_by_xpath(
                '//a[text()="{0}"]'.format(plugin_widget_name_with_dimensions)
            )
        )

        # Wait until the accordion is really loaded
        WebDriverWait(self.selenium, timeout=4).until(
            lambda driver: driver.find_element_by_id('accordion')
        )

        # Add a dummy (1x1) widget
        add_dummy_plugin_widget = self.selenium.find_element_by_xpath(
            '//a[text()="{0}"]'.format(plugin_widget_name_with_dimensions)
        )

        self.selenium.get('{0}'.format(
            add_dummy_plugin_widget.get_attribute('href'))
        )

        # Wait until the add dummy widget form opens
        WebDriverWait(self.selenium, timeout=4).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "standalone")]'
            )
        )

        # Filling with test data
        if form_data:
            for field_name, field_value in form_data.items():
                field_input = self.selenium.find_element_by_name(field_name)
                field_input.send_keys(field_value)

        # If form_hook_func (callable) is specified, call it.
        if form_hook_func:
            form_hook_func()

        # Click add widget button
        add_widget_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        # add_widget_button.click()
        self._click(add_widget_button)  # Unsure

        # Wait until the edit dashboard page opens
        WebDriverWait(self.selenium, timeout=8).until(
            lambda driver: driver.find_element_by_xpath(
                '//div[contains(@class, "{0}")]'.format(
                    plugin_widget_css_class
                )
            )
        )

        # Make sure the success message is there
        self.selenium.find_element_by_xpath(
            """//li[text()='The dashboard widget "{0}" was added """
            """successfully.']""".format(plugin_widget_name)
        )

        dummy_plugin_widget = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )
        dummy_plugin_widget_classes = dummy_plugin_widget.get_attribute(
            'class'
        )
        dummy_plugin_widget_classes = dummy_plugin_widget_classes.split(' ')
        for added_plugin_widget_css_class in added_plugin_widget_css_classes:
            self.assertTrue(added_plugin_widget_css_class
                            in dummy_plugin_widget_classes)

    def __add_dashboard_entry_test(self, wait=0):
        """
        Add dashboard entry test.

        :param int wait: Number of seconds to sleep at the end of the test.
        """
        flow = []

        try:
            # Create dashboard user
            create_dashboard_user()
        except Exception:
            pass

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 1: Dashboard user logs in ++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        def choose_url_image():
            """Hook function to select an image.

            For test 1x1 URL plugin widget.
            """
            image_input = self.selenium.find_element_by_xpath(
                '//select[@name="image"]/option[@value="icon-coffee"]'
            )
            self.assertTrue(image_input is not None)
            # image_input.click()
            self._click(image_input)  # Unsure

        # Test 1x1 URL plugin widget
        self.__add_plugin_widget_test(
            position="col-1 row-1",
            plugin_widget_name="URL",
            plugin_widget_name_with_dimensions="URL (1x1)",
            plugin_widget_css_class="plugin-url_1x1",
            added_plugin_widget_css_classes=('width-1', 'height-1'),
            form_data={'title': "Test 1x1 URL",
                       'url': "http://delusionalinsanity.com/portfolio/"},
            form_hook_func=choose_url_image
        )

        # Test 2x1 Dummy plugin widget
        self.__add_plugin_widget_test(
            position="col-2 row-1",
            plugin_widget_name="Dummy",
            plugin_widget_name_with_dimensions="Dummy (2x1)",
            plugin_widget_css_class="plugin-dummy_2x1",
            added_plugin_widget_css_classes=('width-2', 'height-1')
        )

        # Test 3x3 Memo plugin widget
        self.__add_plugin_widget_test(
            position="col-4 row-1",
            plugin_widget_name="Memo",
            plugin_widget_name_with_dimensions="Memo (3x3)",
            plugin_widget_css_class="plugin-memo_3x3",
            added_plugin_widget_css_classes=('width-3', 'height-3'),
            form_data={'title': "Test 3x3 memo",
                       'text': "Lorem ipsum dolor sit amet."}
        )

        # Test 3x3 Video plugin widget
        self.__add_plugin_widget_test(
            position="col-1 row-2",
            plugin_widget_name="Video",
            plugin_widget_name_with_dimensions="Video (3x3)",
            plugin_widget_css_class="plugin-video_3x3",
            added_plugin_widget_css_classes=('width-3', 'height-3'),
            form_data={'title': "Test 3x3 video",
                       'url': "http://www.youtube.com/watch?v=8GVIui0JK0M"}
        )

        if wait:
            sleep(wait)

        return flow

    def __edit_plugin_widget_test(self,
                                  plugin_widget_name,
                                  plugin_widget_css_class,
                                  form_data={},
                                  form_hook_func=None):
        """Test edit any single plugin.

        :param string plugin_widget_name: Example value "Dummy".
        :param string plugin_widget_css_class: Example value "plugin-dummy1x1".
        :param dict form_data: Example
            value {'title': "Lorem", 'text': "Lorem ipsum dolor sit amet"}.
        :param callable form_hook_func: Function to when edit form is
            opened (to populate the data).

        :example:

        Test 1x1 URL plugin widget::

            def choose_url_image():
                # Hook function to select an image for test 1x1 URL plugin
                # widget.
                image_input = self.selenium.find_element_by_xpath(
                    '//select[@name="image"]/option[@value="icon-coffee"]'
                )
                self.assertTrue(image_input is not None)
                image_input.click()

            self.__edit_plugin_widget_test(
                plugin_widget_name="URL",
                plugin_widget_css_class="plugin-url_1x1",
                form_data = {
                    'title': "Test 1x1 URL",
                    'url': "http://delusionalinsanity.com/portfolio/"
                },
                form_hook_func=choose_url_image
            )

        Test 2x1 Dummy plugin widget::

            self.__edit_plugin_widget_test(
                plugin_widget_name="Dummy",
                plugin_widget_css_class="plugin-dummy_2x1"
            )

        Test 3x3 Memo plugin widget::

            self.__edit_plugin_widget_test(
                plugin_widget_name="Memo",
                plugin_widget_css_class="plugin-memo_3x3",
                form_data={'title': "Lorem",
                           'text': "Lorem ipsum dolor sit amet"}
            )

        Test 3x3 Video plugin widget::

            self.__edit_plugin_widget_test(
                plugin_widget_name="Video",
                plugin_widget_css_class="plugin-video_3x3",
                form_data={
                    'title': "Test 3x3 video",
                    'url': "http://www.youtube.com/watch?v=8GVIui0JK0M"
                }
            )
        """
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 2: User edits the plugin widgets +++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # Click the add widget button to edit the widget on the dashboard
        edit_plugin_widget_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )
        edit_plugin_link = edit_plugin_widget_div.find_element_by_class_name(
            'edit-plugin'
        )
        # edit_plugin_link.click()
        # self._click(edit_plugin_link)  # Unsure
        self._agressive_click(edit_plugin_link)  # Unsure

        # Wait until the edit widget form opens
        WebDriverWait(self.selenium, timeout=8).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "standalone")]'
            )
        )

        # Filling with test data
        if form_data:
            for field_name, field_value in form_data.items():
                field_input = self.selenium.find_element_by_name(field_name)
                field_input.clear()
                field_input.send_keys(field_value)

        # If form_hook_func (callable) is specified, call it.
        if form_hook_func:
            form_hook_func()

        # Click add widget button
        widget_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        # widget_button.click()
        self._click(widget_button)  # Unsure

        # Wait until the edit dashboard page opens
        WebDriverWait(self.selenium, timeout=4).until(
            lambda driver: driver.find_element_by_xpath(
                '//div[contains(@class, "{0}")]'.format(
                    plugin_widget_css_class
                )
            )
        )

        # Make sure the success message is there
        self.selenium.find_element_by_xpath(
            """//li[text()='The dashboard widget "{0}" was edited """
            """successfully.']""".format(plugin_widget_name)
        )

        dummy_plugin_widget = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )

    def __edit_dashboard_entry_test(self, wait=0):
        """Edit dashboard entry test.

        :param int wait: Number of seconds to sleep at the end of the test.
        """
        flow = []

        # Test 1x1 URL plugin widget::

        def choose_url_image():
            # Hook function to select an image for test 1x1 URL plugin widget.
            image_input = self.selenium.find_element_by_xpath(
                '//select[@name="image"]/option[@value="icon-camera"]'
            )
            self.assertTrue(image_input is not None)
            # image_input.click()
            self._click(image_input)  # Unsure

        self.__edit_plugin_widget_test(
            plugin_widget_name="URL",
            plugin_widget_css_class="plugin-url_1x1",
            form_data={
                'title': "Edited test 1x1 URL",
                'url': "http://foreverchild.info/"
            },
            form_hook_func=choose_url_image
        )

        # Test 2x1 Dummy plugin widget::

        self.__edit_plugin_widget_test(
            plugin_widget_name="Dummy",
            plugin_widget_css_class="plugin-dummy_2x1"
        )

        # Test 3x3 Memo plugin widget::

        self.__edit_plugin_widget_test(
            plugin_widget_name="Memo",
            plugin_widget_css_class="plugin-memo_3x3",
            form_data={
                'title': "Edited lorem",
                'text': "Edited lorem ipsum dolor sit amet"
            }
        )

        # Test 3x3 Video plugin widget::

        self.__edit_plugin_widget_test(
            plugin_widget_name="Video",
            plugin_widget_css_class="plugin-video_3x3",
            form_data={
                'title': "Edited test 3x3 video",
                'url': "http://www.youtube.com/watch?v=veOhHqVWwP4"
            }
        )

        if wait:
            sleep(wait)

        return flow

    def __delete_plugin_widget_test(self, plugin_widget_css_class):
        """Test delete any single plugin.

        :param string plugin_widget_css_class: Example value "plugin-dummy1x1".

        :example:

        Test 1x1 URL plugin widget::

            self.__delete_plugin_widget_test(
                plugin_widget_css_class="plugin-url_1x1"
            )

        Test 2x1 Dummy plugin widget::

            self.__delete_plugin_widget_test(
                plugin_widget_css_class="plugin-dummy_2x1"
            )

        Test 3x3 Memo plugin widget::

            self.__delete_plugin_widget_test(
                plugin_widget_css_class="plugin-memo_3x3"
            )

        Test 3x3 Video plugin widget::

            self.__delete_plugin_widget_test(
                plugin_widget_css_class="plugin-video_3x3"
            )
        """
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 2: User deletes the plugin widgets +++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # Click the add widget button to edit the widget on the dashboard
        edit_plugin_widget_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )

        remove_plugin_link = edit_plugin_widget_div.find_element_by_class_name(
            'remove-plugin'
        )
        # remove_plugin_link.click()
        self._click(remove_plugin_link)

        # Wait until the edit dashboard page opens
        WebDriverWait(self.selenium, timeout=8).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "layout")]'
            )
        )

        found = False
        try:
            dummy_plugin_widget = self.selenium.find_element_by_xpath(
                '//div[contains(@class, "{0}")]'.format(
                    plugin_widget_css_class
                )
            )
            found = True
        except Exception:
            pass

        self.assertTrue(not found)

    def __delete_dashboard_entry_test(self, wait=0):
        """Delete dashboard entry test.

        :param int wait: Number of seconds to sleep at the end of the test.
        """
        flow = []

        # Test 1x1 URL plugin widget::

        self.__delete_plugin_widget_test(
            plugin_widget_css_class="plugin-url_1x1"
        )

        # Test 2x1 Dummy plugin widget::

        self.__delete_plugin_widget_test(
            plugin_widget_css_class="plugin-dummy_2x1"
        )

        # Test 3x3 Memo plugin widget::

        self.__delete_plugin_widget_test(
            plugin_widget_css_class="plugin-memo_3x3"
        )

        # Test 3x3 Video plugin widget::

        self.__delete_plugin_widget_test(
            plugin_widget_css_class="plugin-video_3x3"
        )

        if wait:
            sleep(wait)

        return flow

    @print_info
    def test_01_add_dashboard_entry(self):
        """Add dashboard entry test."""
        return self.__add_dashboard_entry_test(wait=WAIT_AT_TEST_END)

    @print_info
    def test_02_edit_dashboard_entry(self):
        """Edit dashboard entry test."""
        self.__add_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        return self.__edit_dashboard_entry_test(wait=WAIT_AT_TEST_END)

    @print_info
    def test_03_delete_dashboard_entry(self):
        """Delete dashboard entry test."""
        self.__add_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        return self.__delete_dashboard_entry_test(wait=WAIT_AT_TEST_END)


if __name__ == '__main__':
    unittest.main()
