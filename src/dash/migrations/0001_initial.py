# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import dash.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout', choices=[(b'android', b'Android'), (b'example', b'Example'), (b'bootstrap2_fluid', b'Bootstrap 2 Fluid'), (b'windows8', b'Windows 8')])),
                ('placeholder_uid', models.CharField(max_length=255, verbose_name='Placeholder')),
                ('plugin_uid', models.CharField(max_length=255, verbose_name='Plugin name', choices=[(b'd3_stacked_to_grouped_bars_chart_5x5', b'Stacked-to-grouped bars chart'), (b'weather_2x2', b'Weather'), (b'chart_4x3', b'Chart'), (b'image_2x1', b'Image'), (b'video_4x4', b'Video'), (b'image_2x3', b'Image'), (b'url_bootstrap_two_2x2', b'URL'), (b'd3_stacked_to_grouped_bars_chart_4x4', b'Stacked-to-grouped bars chart'), (b'd3_sunburst_partition_chart_5x5', b'Sunburst partition chart'), (b'd3_bubble_chart_7x7', b'Bubble Chart'), (b'tinymce_memo_5x5', b'TinyMCE memo'), (b'image_5x4', b'Image'), (b'memo_3x3', b'Memo'), (b'chart_4x5', b'Chart'), (b'd3_sunburst_partition_chart_7x7', b'Sunburst partition chart'), (b'tinymce_memo_4x4', b'TinyMCE memo'), (b'memo_4x4', b'Memo'), (b'video_2x2', b'Video'), (b'url_1x1', b'URL'), (b'memo_1x1', b'Memo'), (b'image_1x2', b'Image'), (b'd3_sunburst_partition_chart_4x4', b'Sunburst partition chart'), (b'image_1x1', b'Image'), (b'chart_5x4', b'Chart'), (b'tinymce_memo_2x2', b'TinyMCE memo'), (b'dummy_3x3', b'Dummy'), (b'chart_2x2', b'Chart'), (b'memo_2x2', b'Memo'), (b'chart_4x4', b'Chart'), (b'video_3x3', b'Video'), (b'url_bootstrap_two_1x1', b'URL'), (b'd3_stacked_to_grouped_bars_chart_7x7', b'Stacked-to-grouped bars chart'), (b'chart_5x5', b'Chart'), (b'url_2x2', b'URL'), (b'dummy_1x1', b'Dummy'), (b'd3_sunburst_partition_chart_6x6', b'Sunburst partition chart'), (b'dummy_1x2', b'Dummy'), (b'tinymce_memo_6x6', b'TinyMCE memo'), (b'dummy_4x4', b'Dummy'), (b'chart_1x1', b'Chart'), (b'chart_1x2', b'Chart'), (b'dummy_5x5', b'Dummy'), (b'news_4x5', b'News'), (b'd3_bubble_chart_5x5', b'Bubble Chart'), (b'video_1x1', b'Video'), (b'dummy_2x2', b'Dummy'), (b'news_2x5', b'News'), (b'dummy_2x1', b'Dummy'), (b'read_rss_feed_3x3', b'Read RSS feed'), (b'weather_3x3', b'Weather'), (b'image_5x5', b'Image'), (b'image_2x2', b'Image'), (b'tinymce_memo_3x3', b'TinyMCE memo'), (b'chart_2x1', b'Chart'), (b'image_4x3', b'Image'), (b'chart_3x4', b'Chart'), (b'chart_3x3', b'Chart'), (b'chart_3x2', b'Chart'), (b'image_4x5', b'Image'), (b'image_4x4', b'Image'), (b'bookmark_1x1', b'Bookmark'), (b'd3_stacked_to_grouped_bars_chart_6x6', b'Stacked-to-grouped bars chart'), (b'image_8x1', b'Image'), (b'memo_5x5', b'Memo'), (b'read_rss_feed_2x3', b'Read RSS feed'), (b'd3_bubble_chart_4x4', b'Bubble Chart'), (b'image_3x8', b'Image'), (b'video_6x6', b'Video'), (b'chart_2x3', b'Chart'), (b'memo_6x6', b'Memo'), (b'image_3x4', b'Image'), (b'd3_bubble_chart_6x6', b'Bubble Chart'), (b'video_5x5', b'Video'), (b'image_3x2', b'Image'), (b'image_3x3', b'Image')])),
                ('plugin_data', models.TextField(null=True, verbose_name='Plugin data', blank=True)),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Position', blank=True)),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dashboard entry',
                'verbose_name_plural': 'Dashboard entries',
            },
        ),
        migrations.CreateModel(
            name='DashboardPlugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_uid', models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False, choices=[(b'd3_stacked_to_grouped_bars_chart_5x5', b'Stacked-to-grouped bars chart'), (b'weather_2x2', b'Weather'), (b'chart_4x3', b'Chart'), (b'image_2x1', b'Image'), (b'video_4x4', b'Video'), (b'image_2x3', b'Image'), (b'url_bootstrap_two_2x2', b'URL'), (b'd3_stacked_to_grouped_bars_chart_4x4', b'Stacked-to-grouped bars chart'), (b'd3_sunburst_partition_chart_5x5', b'Sunburst partition chart'), (b'd3_bubble_chart_7x7', b'Bubble Chart'), (b'tinymce_memo_5x5', b'TinyMCE memo'), (b'image_5x4', b'Image'), (b'memo_3x3', b'Memo'), (b'chart_4x5', b'Chart'), (b'd3_sunburst_partition_chart_7x7', b'Sunburst partition chart'), (b'tinymce_memo_4x4', b'TinyMCE memo'), (b'memo_4x4', b'Memo'), (b'video_2x2', b'Video'), (b'url_1x1', b'URL'), (b'memo_1x1', b'Memo'), (b'image_1x2', b'Image'), (b'd3_sunburst_partition_chart_4x4', b'Sunburst partition chart'), (b'image_1x1', b'Image'), (b'chart_5x4', b'Chart'), (b'tinymce_memo_2x2', b'TinyMCE memo'), (b'dummy_3x3', b'Dummy'), (b'chart_2x2', b'Chart'), (b'memo_2x2', b'Memo'), (b'chart_4x4', b'Chart'), (b'video_3x3', b'Video'), (b'url_bootstrap_two_1x1', b'URL'), (b'd3_stacked_to_grouped_bars_chart_7x7', b'Stacked-to-grouped bars chart'), (b'chart_5x5', b'Chart'), (b'url_2x2', b'URL'), (b'dummy_1x1', b'Dummy'), (b'd3_sunburst_partition_chart_6x6', b'Sunburst partition chart'), (b'dummy_1x2', b'Dummy'), (b'tinymce_memo_6x6', b'TinyMCE memo'), (b'dummy_4x4', b'Dummy'), (b'chart_1x1', b'Chart'), (b'chart_1x2', b'Chart'), (b'dummy_5x5', b'Dummy'), (b'news_4x5', b'News'), (b'd3_bubble_chart_5x5', b'Bubble Chart'), (b'video_1x1', b'Video'), (b'dummy_2x2', b'Dummy'), (b'news_2x5', b'News'), (b'dummy_2x1', b'Dummy'), (b'read_rss_feed_3x3', b'Read RSS feed'), (b'weather_3x3', b'Weather'), (b'image_5x5', b'Image'), (b'image_2x2', b'Image'), (b'tinymce_memo_3x3', b'TinyMCE memo'), (b'chart_2x1', b'Chart'), (b'image_4x3', b'Image'), (b'chart_3x4', b'Chart'), (b'chart_3x3', b'Chart'), (b'chart_3x2', b'Chart'), (b'image_4x5', b'Image'), (b'image_4x4', b'Image'), (b'bookmark_1x1', b'Bookmark'), (b'd3_stacked_to_grouped_bars_chart_6x6', b'Stacked-to-grouped bars chart'), (b'image_8x1', b'Image'), (b'memo_5x5', b'Memo'), (b'read_rss_feed_2x3', b'Read RSS feed'), (b'd3_bubble_chart_4x4', b'Bubble Chart'), (b'image_3x8', b'Image'), (b'video_6x6', b'Video'), (b'chart_2x3', b'Chart'), (b'memo_6x6', b'Memo'), (b'image_3x4', b'Image'), (b'd3_bubble_chart_6x6', b'Bubble Chart'), (b'video_5x5', b'Video'), (b'image_3x2', b'Image'), (b'image_3x3', b'Image')])),
                ('groups', models.ManyToManyField(to='auth.Group', null=True, verbose_name='Group', blank=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='User', blank=True)),
            ],
            options={
                'verbose_name': 'Dashboard plugin',
                'verbose_name_plural': 'Dashboard plugins',
            },
        ),
        migrations.CreateModel(
            name='DashboardSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout', choices=[(b'android', b'Android'), (b'example', b'Example'), (b'bootstrap2_fluid', b'Bootstrap 2 Fluid'), (b'windows8', b'Windows 8')])),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('is_public', models.BooleanField(default=False, help_text='Makes your dashboard to be visible to the public. Visibility of workspaces could be adjust separately for each workspace, however setting your dashboard to be visible to public, makes your default workspace visible to public too.', verbose_name='Is public?')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'Dashboard settings',
                'verbose_name_plural': 'Dashboard settings',
            },
        ),
        migrations.CreateModel(
            name='DashboardWorkspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout', choices=[(b'android', b'Android'), (b'example', b'Example'), (b'bootstrap2_fluid', b'Bootstrap 2 Fluid'), (b'windows8', b'Windows 8')])),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(verbose_name='Slug', unique=True, editable=False)),
                ('position', dash.fields.OrderField(null=True, verbose_name='Position', blank=True)),
                ('is_public', models.BooleanField(default=False, help_text='Makes your workspace to be visible to the public.', verbose_name='Is public?')),
                ('is_clonable', models.BooleanField(default=False, help_text='Makes your workspace to be cloneable by other users.', verbose_name='Is cloneable?')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dashboard workspace',
                'verbose_name_plural': 'Dashboard workspaces',
            },
        ),
        migrations.AddField(
            model_name='dashboardentry',
            name='workspace',
            field=models.ForeignKey(verbose_name='Workspace', blank=True, to='dash.DashboardWorkspace', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='dashboardworkspace',
            unique_together=set([('user', 'slug'), ('user', 'name')]),
        ),
    ]
