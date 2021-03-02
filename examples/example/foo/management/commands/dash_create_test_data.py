from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

from dash.contrib.layouts.android.dash_layouts import (
    AndroidLayout,
    AndroidMainPlaceholder,
    AndroidShortcutsPlaceholder,
)
from dash.models import DashboardSettings, DashboardWorkspace, DashboardEntry
from dash.tests import (
    create_dashboard_user,
    DASH_TEST_USER_PASSWORD,
    DASH_TEST_USER_USERNAME,
)


def clean_extra_spaces(val):
    """Clean extra spaces."""
    return ' '.join(val.split())


def create_dashboard_entries(user, workspace=None, mixed_order=False):
    """Create dashboard entries.

    :param django.contrib.auth.models.User user:
    :param dash.models.DashboardWorkspace workspace:
    :param bool mixed_order:
    """
    # *********************************
    # *********************************
    # ******** Main placeholder *******
    # *********************************
    # *********************************
    buf = []

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://delusionalinsanity.com/portfolio/",
                "image": "icon-picture",
                "external": true,
                "title": "Photography"
            }
            """
        ),
        position=(2 if mixed_order else 1)
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://f0reverchild.livejournal.com/",
                "image": "icon-book",
                "external": true,
                "title": "Livejournal"
            }
            """
        ),
        position=(1 if mixed_order else 2)
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.modelmayhem.com/95855",
                "image": "icon-camera",
                "external": true,
                "title": "Model Mayhem"
            }
            """
        ),
        position=(30 if mixed_order else 3)
    )
    buf.append(dashboard_entry)

    # TinyMCE plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='tinymce_memo_3x3',
        plugin_data=clean_extra_spaces(
            '{\"text\": \"<p>Python is my personal (and primary) programming '
            'language of choice and also happens to be the primary '
            'programming language at my beloved company, Goldmund, '
            'Wyldebeast &amp; Wunderliebe. So, when starting to work with a '
            'new technology, I prefer to use a clean and easy (Pythonic!) '
            'API.<br/ ><br/ >After studying tons of articles on the web, '
            'reading (and writing) white papers, and doing basic performance '
            'tests (sometimes hard if you\'re on a tight schedule), my '
            'company recently selected Cloudera for our Big Data platform '
            '(including using Apache HBase as our data store for Apache '
            'Hadoop), with Cloudera Manager serving a role as \\\"one '
            'console to rule them all.\\\"...<a href=\\\"http://blog.'
            'cloudera.com/blog/2013/10/hello-starbase-a-python-wrapper-'
            'for-the-hbase-rest-api/\\\" target=\\\"_blank\\\">(read more)'
            '</a></p>\", \"title\": \"Starbase: A Python Wrapper for the '
            'HBase REST API\"}'
        ),
        position=(7 if mixed_order else 4)
    )
    buf.append(dashboard_entry)

    # BigVideo plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='video_3x3',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.youtube.com/watch?v=8GVIui0JK0M",
                "title": "Test 3x3 video"
            }
            """
        ),
        position=(4 if mixed_order else 7)
    )
    buf.append(dashboard_entry)

    # Memo plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='memo_2x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "(1) Dragging of widgets (within the Placeholder),
                         (2) Reset dashboards triggers/hoocks,
                         (3) Pre-defined template system for workspaces (with
                             plugins in),
                         (4) Copy/paste widgets between workspaces.",
                "title": "django-dash TODOs"
            }
            """
        ),
        position=22
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "https://github.com/barseghyanartur",
                "image": "icon-github",
                "external": true, "title": "GitHub"
            }
            """
        ),
        position=(27 if mixed_order else 24)
    )
    buf.append(dashboard_entry)

    # LargeDummy plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='dummy_2x1',
        plugin_data=clean_extra_spaces(
            """
            {
            "text": "\u0531\u0578\u0582\u0581\u057f\u0585\u0580.
            \u0531\u0576\u057f\u0565
            \u056b\u0561\u0581\u0578\u0582\u056c\u056b\u057d.
            \u0555\u0564\u056b\u0585 \u0581\u0578\u0582\u0580\u0561\u0565.
            \u0554\u0578\u0582\u0561\u0574
            \u057a\u0580\u056b\u0574\u056b\u057d
            \u0570\u0568\u0574\u0565\u0576\u0561\u0565\u0585\u057d
            \u057a\u0565\u0576\u0561\u057f\u056b\u0562\u0578\u0582\u057d
            \u0561\u0578\u0582\u0563\u0578\u0582\u0565
            \u0578\u0582\u0580\u0576\u0561.
            \u053c\u056b\u057f\u0585\u0580\u0561
            \u0562\u056b\u0562\u0565\u0576\u0564\u0578\u0582\u0574
            \u0576\u0578\u0582\u056c\u056c\u0561
            \u0586\u0561\u0578\u0582\u0581\u056b\u0562\u0578\u0582\u057d.
            \u0544\u0561\u057d\u057d\u0561...",
            "lipsum_max_chars": 130,
            "lipsum_language": "hy",
            "show_title": false,
            "generate_lipsum": true
            }
            """
        ),
        position=25
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "https://barseghyanartur.blogspot.com/",
                "image": "icon-info-sign",
                "external": true,
                "title": "Blogspot"
            }
            """
        ),
        position=(24 if mixed_order else 27)
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "https://bitbucket.org/barseghyanartur",
                "image": "icon-bitbucket",
                "external": true,
                "title": "BitBucket"
            }
            """
        ),
        position=(3 if mixed_order else 30)
    )
    buf.append(dashboard_entry)

    # *********************************
    # *********************************
    # ***** Shortcuts placeholder *****
    # *********************************
    # *********************************

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.goldmund-wyldebeast-wunderliebe.com/",
                "image": "icon-thumbs-up",
                "external": true,
                "title": "Goldmund, Wyldebeast & Wunderliebe"
            }
            """
        ),
        position=(2 if mixed_order else 1)
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://foreverchild.info/",
                "image": "icon-star",
                "external": true,
                "title": "Forever Child"
            }
            """
        ),
        position=(1 if mixed_order else 2)
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.youtube.com/watch?v=gDyujx0BZSg",
                "image": "icon-youtube",
                "external": true,
                "title": "Cocteau Twins - Treasure"
            }
            """
        ),
        position=3
    )
    buf.append(dashboard_entry)

    # Dummy plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=4
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.youtube.com/watch?v=tiYr-464-Nc",
                "image": "icon-youtube",
                "external": true,
                "title": "Portishead - Third"
            }
            """
        ),
        position=5
    )
    buf.append(dashboard_entry)

    # Dummy plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=6
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.youtube.com/watch?v=7SFf2sQb4H4",
                "image": "icon-youtube",
                "external": true,
                "title": "Lais - Kanneke (tiens bien)"
            }
            """
        ),
        position=7
    )
    buf.append(dashboard_entry)

    # LargeDummy portrait plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=8
    )
    buf.append(dashboard_entry)

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://www.youtube.com/watch?v=67JH3e7d1r4",
                "image": "icon-youtube",
                "external": true,
                "title": "Paradise Lost - Draconian Times"
            }
            """
        ),
        position=10
    )
    buf.append(dashboard_entry)

    # Bulk insert
    DashboardEntry._default_manager.bulk_create(buf)


def create_news_and_rss_dashboard_entries(user, workspace):
    """Dashboard entries for news page.

    :param django.contrib.auth.models.User user:
    :param dash.models.DashboardWorkspace workspace:
    """
    buf = []

    # *********************************
    # *********************************
    # ***** Shortcuts placeholder *****
    # *********************************
    # *********************************

    # URL plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='url_1x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "url": "http://delusionalinsanity.com/portfolio/",
                "image": "icon-picture",
                "external": true,
                "title": "Delusional Insanity"
            }
            """
        ),
        position=1
    )
    buf.append(dashboard_entry)

    # LargeDummy portrait plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=2
    )
    buf.append(dashboard_entry)

    # LargeDummy portrait plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=4
    )
    buf.append(dashboard_entry)

    # LargeDummy portrait plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=6
    )
    buf.append(dashboard_entry)

    # LargeDummy portait plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidShortcutsPlaceholder.uid,
        plugin_uid='dummy_1x2',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "",
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": false
            }
            """
        ),
        position=8
    )
    buf.append(dashboard_entry)

    # *********************************
    # *********************************
    # ******** Main placeholder *******
    # *********************************
    # *********************************

    # News plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='news_4x5',
        plugin_data=clean_extra_spaces(
            """
            {
                "truncate_after": 35,
                "max_items": 5,
                "show_title": true,
                "cache_for": 3600
            }
            """
        ),
        position=1
    )
    buf.append(dashboard_entry)

    # RSS feed plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='read_rss_feed_2x3',
        plugin_data=clean_extra_spaces(
            """
            {
                "custom_feed_title": "News feed",
                "truncate_after": 35,
                "feed_url": "http://foreverchild.info/rss/",
                "cache_for": 3600,
                "show_feed_title": true,
                "max_items": 6
            }
            """
        ),
        position=5
    )
    buf.append(dashboard_entry)

    # LargeDummy plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='dummy_2x1',
        plugin_data=clean_extra_spaces(
            """
            {
            "text": "\u03a3\u03bfc\u03b9\u03b9\u03c3 \u03b5\u03b3\u03b5\u03c4
            \u03c4\u03b9\u03bdc\u03b9\u03b4\u03b8\u03bd\u03c4 \u03b1c,
            \u03c6\u03c1\u03b9\u03bd\u03b3\u03b9\u03bb\u03bb\u03b1
            \u03b1c. V\u03b5 \u03b1\u03b8c\u03c4\u03bf\u03c1
            \u03b8\u03c4 \u03c0\u03c1\u03b1\u03b5\u03c3\u03b5\u03bd\u03c4
            v\u03b1\u03c1\u03b9\u03b8\u03c3,
            \u03bf\u03c1\u03bd\u03b1\u03c1\u03b5 \u03bd\u03b5c,
            \u03b1\u03b8c\u03c4\u03bf\u03c1, \u03b1\u03b4,
            \u03bb\u03bf\u03c1\u03b5\u03bc
            c\u03bf\u03bd\u03b4\u03b9\u03bc\u03b5\u03bd\u03c4\u03b8\u03bc.
            \u03a0\u03bf\u03c4\u03b5\u03bd\u03c4\u03b9.
            \u0391\u03bb\u03b9q\u03b8\u03b1\u03bc.
            \u03a3\u03bf\u03bb\u03bb\u03b9c\u03b9\u03c4\u03b8\u03b4\u03b9\u03bd
            \u03b4\u03b9c\u03c4\u03b8\u03bc \u03b8\u03c4
            \u03bd\u03bf\u03c3\u03c4\u03c1\u03b1 \u03b4\u03b9\u03c3.
            \u0391\u03bd\u03c4\u03b5 c\u03bf\u03bd\u03b8\u03b2\u03b9\u03b1
            \u03c1\u03b8\u03c4\u03c1\u03b8\u03bc,
            \u03c0\u03b7\u03b1\u03c3\u03b5\u03bb\u03bb\u03b8\u03c3 ...",
            "lipsum_max_chars": 200,
            "lipsum_language": "el",
            "show_title": false,
            "generate_lipsum": true
            }
            """
        ),
        position=23
        )
    buf.append(dashboard_entry)

    # LargeDummy plugin
    dashboard_entry = DashboardEntry(
        user=user,
        workspace=workspace,
        layout_uid=AndroidLayout.uid,
        placeholder_uid=AndroidMainPlaceholder.uid,
        plugin_uid='dummy_2x1',
        plugin_data=clean_extra_spaces(
            """
            {
                "text": "Quis inceptos. Urna libero tortor nonummy pretium.
                         Lectus. Platea eu, ligula lacinia dis, parturient
                         consequat. Nunc tempor pretium natoque cubilia nunc.
                         Ligula at, nulla. Congue at. Mauris. Luctus...",
                "lipsum_max_chars": 200,
                "lipsum_language": "en",
                "show_title": false,
                "generate_lipsum": true
            }
            """
        ),
        position=29
    )
    buf.append(dashboard_entry)

    # Bulk insert
    DashboardEntry._default_manager.bulk_create(buf)


class Command(BaseCommand):
    """Creates test data to fill the dashboard with."""

    def handle(self, *args, **options):
        """Handle."""
        try:
            create_dashboard_user()
        except Exception:
            pass

        User = get_user_model()
        user = User._default_manager.get(username=DASH_TEST_USER_USERNAME)

        # *************************************************************
        # *********************** Sync plugins ************************
        # *************************************************************
        call_command('dash_sync_plugins', verbosity=3, interactive=False)

        # *************************************************************
        # ****************** Create dashboard settings ****************
        # *************************************************************
        dashboard_settings = DashboardSettings(
            user=user,
            title=_("Test dashboard"),
            is_public=True
        )
        dashboard_settings.save()

        # *************************************************************
        # ****** Create dashboard entries for default workspace *******
        # *************************************************************
        create_dashboard_entries(user=user)

        # *************************************************************
        # ***** Create dashboard workspace with regrouped entries *****
        # *************************************************************
        dashboard_workspace = DashboardWorkspace(
            user=user,
            layout_uid=AndroidLayout.uid,
            name=_("Default workspace reordered"),
            slug='reordered-default-workspace',
            is_public=False
        )
        dashboard_workspace.save()

        # *************************************************************
        # ** Create dashboard entries for "Test workspace" workspace **
        # *************************************************************
        create_dashboard_entries(user=user,
                                 workspace=dashboard_workspace,
                                 mixed_order=True)

        # *************************************************************
        # *** Create dashboard workspace for news & rss feed entries **
        # *************************************************************
        dashboard_workspace = DashboardWorkspace(
            user=user,
            layout_uid=AndroidLayout.uid,
            name=_("News and RSS feed"),
            slug='news-and-rss-feed',
            is_public=False
        )
        dashboard_workspace.save()

        # *************************************************************
        # ** Create dashboard entries for "Test workspace" workspace **
        # *************************************************************
        create_news_and_rss_dashboard_entries(user=user,
                                              workspace=dashboard_workspace)
