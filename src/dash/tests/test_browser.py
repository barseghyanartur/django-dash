from time import sleep
import unittest

from django.conf import settings
from django.core.management import call_command
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait

from ..settings import WAIT_BETWEEN_TEST_STEPS, WAIT_AT_TEST_END
from .base import (
    log_info,
    setup_dash,
    create_dashboard_user,
    DASH_TEST_USER_USERNAME,
    DASH_TEST_USER_PASSWORD,
)

__title__ = 'dash.tests'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'DashBrowserTest',
)


class DashBrowserTest(StaticLiveServerTestCase):
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
        chrome_driver_path = getattr(
            settings,
            'CHROME_DRIVER_EXECUTABLE_PATH',
            None
        )
        chrome_driver_options = getattr(
            settings,
            'CHROME_DRIVER_OPTIONS',
            None
        )
        firefox_bin_path = getattr(settings, 'FIREFOX_BIN_PATH', None)
        phantom_js_executable_path = getattr(
            settings, 'PHANTOM_JS_EXECUTABLE_PATH', None
        )
        if chrome_driver_path is not None:
            cls.selenium = webdriver.Chrome(
                executable_path=chrome_driver_path,
                options=chrome_driver_options
            )
        elif phantom_js_executable_path is not None:
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

    def _sleep(self, secs=10):
        sleep(secs)

    def _click(self, element):
        """Click on any element."""
        # self.selenium.execute_script("$(arguments[0]).click();", element)
        self.selenium.execute_script("arguments[0].click();", element)

    def _agressive_click(self, element):
        """Agressive click."""
        link = element.get_attribute('href')
        self.selenium.get(link)

    def __login(self):
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 1: Dashboard user logs in ++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        try:
            # Create dashboard user
            create_dashboard_user()
        except Exception:
            pass

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

    def __add_plugin_widget_test(self,
                                 position,
                                 plugin_widget_name,
                                 plugin_widget_name_with_dimensions,
                                 plugin_widget_css_class,
                                 added_plugin_widget_css_classes,
                                 form_data={},
                                 form_hook_func=None,
                                 do_login=True):
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
        if do_login:
            # Login
            self.__login()

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

    def __add_dashboard_entry_test(self, wait=0, do_login=True):
        """
        Add dashboard entry test.

        :param int wait: Number of seconds to sleep at the end of the test.
        """
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
            form_data={
                'title': "Test 1x1 URL",
                'url': "http://delusionalinsanity.com/portfolio/",
            },
            form_hook_func=choose_url_image,
            do_login=do_login
        )

        # Test 2x1 Dummy plugin widget
        self.__add_plugin_widget_test(
            position="col-2 row-1",
            plugin_widget_name="Dummy",
            plugin_widget_name_with_dimensions="Dummy (2x1)",
            plugin_widget_css_class="plugin-dummy_2x1",
            added_plugin_widget_css_classes=('width-2', 'height-1'),
            do_login=do_login
        )

        # Test 3x3 Memo plugin widget
        self.__add_plugin_widget_test(
            position="col-4 row-1",
            plugin_widget_name="Memo",
            plugin_widget_name_with_dimensions="Memo (3x3)",
            plugin_widget_css_class="plugin-memo_3x3",
            added_plugin_widget_css_classes=('width-3', 'height-3'),
            form_data={
                'title': "Test 3x3 memo",
                'text': "Lorem ipsum dolor sit amet.",
            },
            do_login=do_login
        )

        # Test 3x3 Video plugin widget
        self.__add_plugin_widget_test(
            position="col-1 row-2",
            plugin_widget_name="Video",
            plugin_widget_name_with_dimensions="Video (3x3)",
            plugin_widget_css_class="plugin-video_3x3",
            added_plugin_widget_css_classes=('width-3', 'height-3'),
            form_data={
                'title': "Test 3x3 video",
                'url': "http://www.youtube.com/watch?v=8GVIui0JK0M",
            },
            do_login=do_login
        )

        if wait:
            sleep(wait)

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
        # Test 1x1 URL plugin widget::

        def choose_url_image():
            # Hook function to select an image for test 1x1 URL plugin widget.
            image_input = self.selenium.find_element_by_xpath(
                '//select[@name="image"]/option[@value="icon-camera"]'
            )
            self.assertTrue(image_input is not None)
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

    def __delete_plugin_widget_test(self, plugin_widget_css_class):
        """Test delete any single plugin widget.

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
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                '//body[contains(@class, "layout")]'
            )
        )

        self._sleep(2)
        found = False
        try:
            plugin_widget = self.selenium.find_element_by_xpath(
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
            self._sleep(wait)

    def __copy_plugin_widget_test(self, plugin_widget_css_class):
        """Test copy any single plugin widget.

        :param string plugin_widget_css_class: Example value "plugin-dummy1x1".

        :example:

        Test 1x1 URL plugin widget::

            self.__copy_plugin_widget_test(
                plugin_widget_css_class="plugin-url_1x1"
            )

        Test 2x1 Dummy plugin widget::

            self.__copy_plugin_widget_test(
                plugin_widget_css_class="plugin-dummy_2x1"
            )

        Test 3x3 Memo plugin widget::

            self.__copy_plugin_widget_test(
                plugin_widget_css_class="plugin-memo_3x3"
            )

        Test 3x3 Video plugin widget::

            self.__copy_plugin_widget_test(
                plugin_widget_css_class="plugin-video_3x3"
            )
        """
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++ Step 2: User copies the plugin widgets ++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        # Click the add widget button to edit the widget on the dashboard
        edit_plugin_widget_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )

        copy_plugin_link = edit_plugin_widget_div.find_element_by_class_name(
            'copy-plugin'
        )
        # remove_plugin_link.click()
        self._click(copy_plugin_link)

        # Wait until the edit dashboard page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'was successfully copied and """
                """placed into the clipboard') """
                """and contains(@class, "alert-info")]"""
            )
        )

    def __create_dashboard_workspace_test(self, wait=0, do_login=True):
        """Test create dashboard workspace."""
        if do_login:
            # Login
            self.__login()
        # Click the menu button to create a new workspace
        menu_div = self.selenium.find_element_by_xpath(
            '//a[contains(@class, "menu-dashboard-settings")]'
        )
        # Click on it
        self._click(menu_div)

        # Wait until the create workspace link is visible
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//a[contains(@title, 'Create a workspace') """
                """and contains(@class, "menu-dashboard-create-workspace")]"""
            )
        )

        # Get the create workspace link element
        create_workspace_link = self.selenium.find_element_by_xpath(
            """//a[contains(@title, 'Create a workspace') """
            """and contains(@class, "menu-dashboard-create-workspace")]"""
        )
        # Click on it
        self._click(create_workspace_link)

        # Wait until the create dashboard dialogue opens up
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//h2[contains(text(), 'Add dashboard workspace') """
                """and contains(@class, "content-title")]"""
            )
        )

        self._sleep(2)

        # Fill in the value
        field_input = self.selenium.find_element_by_name('name')
        field_input.send_keys("Copy workspace")

        # Click add widget button
        submit_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        submit_button.click()

        # Wait until the new page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'The dashboard workspace "Copy """
                """workspace" was created successfully.') """
                """and contains(@class, "alert-info")]"""
            )
        )

        if wait:
            sleep(wait)

    def __edit_dashboard_workspace_test(self, wait=0):
        """Test edit dashboard workspace."""
        # Click the menu button to create a new workspace
        menu_div = self.selenium.find_element_by_xpath(
            '//a[contains(@class, "menu-dashboard-settings")]'
        )
        # Click on it
        self._click(menu_div)

        # Wait until the create workspace link is visible
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//a[contains(@title, 'Edit current workspace') """
                """and contains(@class, "menu-dashboard-edit-workspace")]"""
            )
        )

        # Get the edit workspace link element
        edit_workspace_link = self.selenium.find_element_by_xpath(
            """//a[contains(@title, 'Edit current workspace') """
            """and contains(@class, "menu-dashboard-edit-workspace")]"""
        )
        # Click on it
        self._click(edit_workspace_link)

        # Wait until the edit dashboard dialogue opens up
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//h2[contains(text(), 'Edit dashboard workspace') """
                """and contains(@class, "content-title")]"""
            )
        )

        self._sleep(2)

        # Fill in the value
        field_input = self.selenium.find_element_by_name('is_public')
        field_input.send_keys(True)

        field_input = self.selenium.find_element_by_name('is_cloneable')
        field_input.send_keys(True)

        # Click add widget button
        submit_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit"]'
        )
        submit_button.click()

        # Wait until the new page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'The dashboard workspace "Copy """
                """workspace" was edited successfully.') """
                """and contains(@class, "alert-info")]"""
            )
        )

        if wait:
            sleep(wait)

    def __clone_dashboard_workspace_test(self, wait=0):
        """Test clone dashboard workspace."""
        # Click the menu button to create a new workspace
        menu_div = self.selenium.find_element_by_xpath(
            '//a[contains(@class, "menu-dashboard-settings")]'
        )
        # Click on it
        self._click(menu_div)

        # Wait until the create workspace link is visible
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//a[contains(@title, 'Clone current workspace') """
                """and contains(@class, "menu-dashboard-clone-workspace")]"""
            )
        )

        # Get the clone workspace link element
        clone_workspace_link = self.selenium.find_element_by_xpath(
            """//a[contains(@title, 'Clone current workspace') """
            """and contains(@class, "menu-dashboard-clone-workspace")]"""
        )
        # Click on it
        self._click(clone_workspace_link)

        # Wait until the new page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'Dashboard workspace `Copy """
                """workspace` was successfully cloned into') """
                """and contains(@class, "alert-info")]"""
            )
        )

        if wait:
            sleep(wait)

    def __delete_dashboard_workspace_test(self, wait=0):
        """Test delete dashboard workspace."""
        # Click the menu button to create a new workspace
        menu_div = self.selenium.find_element_by_xpath(
            '//a[contains(@class, "menu-dashboard-settings")]'
        )
        # Click on it
        self._click(menu_div)

        # Wait until the delete workspace link is visible
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//a[contains(@title, 'Delete current workspace') """
                """and contains(@class, "menu-dashboard-delete-workspace")]"""
            )
        )

        # Get the delete workspace link element
        clone_workspace_link = self.selenium.find_element_by_xpath(
            """//a[contains(@title, 'Delete current workspace') """
            """and contains(@class, "menu-dashboard-delete-workspace")]"""
        )
        # Click on it
        self._click(clone_workspace_link)

        # Wait until the delete dashboard dialogue opens up
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//h2[contains(text(), 'Delete dashboard workspace') """
                """and contains(@class, "content-title")]"""
            )
        )

        self._sleep(2)

        # Click add widget button
        submit_button = self.selenium.find_element_by_xpath(
            '//button[@type="submit" and contains(@name, "delete")]'
        )
        submit_button.click()

        # Wait until the new page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'The dashboard workspace "Copy """
                """workspace') """
                """and contains(text(), 'was deleted successfully')"""
                """and contains(@class, "alert-info")]"""
            )
        )

        if wait:
            sleep(wait)

    def __paste_plugin_widget_test(self, plugin_widget_css_class, wait=0):
        """Test paste any single plugin widget.

        :param string plugin_widget_css_class: Example value
            "empty-widget-cell col-1 row-1".
        """
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ++++++++++ Step 2: User pastes the copied plugin widgets ++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Click the add widget button to edit the widget on the dashboard
        add_plugin_widget_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "{0}")]'.format(plugin_widget_css_class)
        )
        add_plugin_link = add_plugin_widget_div.find_element_by_tag_name('a')
        self._click(add_plugin_link)

        # Wait until the widget dialog opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//h2[contains(text(), 'Widgets') """
                """and contains(@class, "content-title")]"""
            )
        )

        self._sleep(2)

        # Find paste element
        paste_div = self.selenium.find_element_by_xpath(
            '//div[contains(@class, "paste-from-clipboard")]'
        )
        # Click it
        paste_link = paste_div.find_element_by_tag_name('a')
        self._click(paste_link)

        # Wait until the new page opens
        WebDriverWait(self.selenium, timeout=16).until(
            lambda driver: driver.find_element_by_xpath(
                """//li[contains(text(), 'was successfully pasted """
                """from clipboard') """
                """and contains(@class, "alert-info")]"""
            )
        )

        if wait:
            sleep(wait)

    def __copy_dashboard_entry_test(self, wait=0):
        """Copy dashboard entry test.

        :param int wait: Number of seconds to sleep at the end of the test.
        """
        # Test 1x1 URL plugin widget::

        self.__copy_plugin_widget_test(
            plugin_widget_css_class="plugin-url_1x1"
        )

        # Test 2x1 Dummy plugin widget::

        self.__copy_plugin_widget_test(
            plugin_widget_css_class="plugin-dummy_2x1"
        )

        # Test 3x3 Memo plugin widget::

        self.__copy_plugin_widget_test(
            plugin_widget_css_class="plugin-memo_3x3"
        )

        # Test 3x3 Video plugin widget::

        self.__copy_plugin_widget_test(
            plugin_widget_css_class="plugin-video_3x3"
        )

        if wait:
            sleep(wait)

    @log_info
    def test_01_add_dashboard_entry(self):
        """Add dashboard entry test."""
        return self.__add_dashboard_entry_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_02_edit_dashboard_entry(self):
        """Edit dashboard entry test."""
        self.__add_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        self.__edit_dashboard_entry_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_03_delete_dashboard_entry(self):
        """Delete dashboard entry test."""
        self.__add_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        self.__delete_dashboard_entry_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_04_create_dashboard_workspace(self):
        """Create dashboard workspace test."""
        self.__create_dashboard_workspace_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_05_copy_paste_dashboard_entry(self):
        """Copy/paste dashboard entry test."""
        self.__add_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        self.__copy_dashboard_entry_test(wait=WAIT_BETWEEN_TEST_STEPS)
        self.__create_dashboard_workspace_test(
            wait=WAIT_BETWEEN_TEST_STEPS,
            do_login=False
        )
        self.__paste_plugin_widget_test(
            'empty-widget-cell col-1 row-1',
            wait=WAIT_AT_TEST_END
        )

    @log_info
    def test_06_add_dashboard_entry_to_workspace(self):
        """Add dashboard entry to workspace test."""
        self.__create_dashboard_workspace_test(wait=WAIT_AT_TEST_END)
        self.__add_dashboard_entry_test(wait=WAIT_AT_TEST_END, do_login=False)

    @log_info
    def test_07_edit_dashboard_workspace(self):
        """Edit dashboard workspace test."""
        self.__create_dashboard_workspace_test(wait=WAIT_AT_TEST_END)
        self.__edit_dashboard_workspace_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_08_clone_dashboard_workspace(self):
        """Clone dashboard workspace test."""
        self.__create_dashboard_workspace_test(wait=WAIT_AT_TEST_END)
        self.__add_dashboard_entry_test(wait=WAIT_AT_TEST_END, do_login=False)
        self.__clone_dashboard_workspace_test(wait=WAIT_AT_TEST_END)

    @log_info
    def test_09_delete_dashboard_workspace(self):
        """Clone dashboard workspace test."""
        self.__create_dashboard_workspace_test(wait=WAIT_AT_TEST_END)
        self.__delete_dashboard_workspace_test(wait=WAIT_AT_TEST_END)


if __name__ == '__main__':
    unittest.main()
