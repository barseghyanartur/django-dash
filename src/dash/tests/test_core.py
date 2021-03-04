import unittest

from django.contrib.auth import get_user_model
from django.test import (
    TestCase,
    RequestFactory,
)

from ..base import (
    get_layout,
    get_registered_layouts,
)
from ..models import DashboardEntry
from ..utils import get_occupied_cells, get_user_plugins
from .base import (
    log_info,
    setup_dash,
    create_dashboard_user,
    DASH_TEST_USER_USERNAME,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'DashCoreTest',
)


class DashCoreTest(TestCase):
    """Tests of django-dash core functionality."""

    def setUp(self):
        setup_dash()

    @log_info
    def test_01_registered_layouts(self):
        """Test registered layouts (`get_registered_layouts`)."""
        res = get_registered_layouts()
        self.assertTrue(len(res) > 0)
        return res

    @log_info
    def test_02_active_layout(self):
        """Test active layout (`get_layout`)."""
        layout_cls = get_layout()
        self.assertTrue(layout_cls is not None)
        return layout_cls

    @log_info
    def test_03_get_layout_placeholders(self):
        """Test active layout placeholders (`get_placeholder_instances`)."""
        layout_cls = get_layout()
        layout = layout_cls()
        res = layout.get_placeholder_instances()
        self.assertTrue(len(res) > 0)
        return res

    @log_info
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

    @log_info
    def test_05_get_occupied_cells(self):
        """Test ``dash.utils.get_occupied_cells``."""
        # Fake dashboard entry
        class Entry:
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


if __name__ == '__main__':
    unittest.main()
