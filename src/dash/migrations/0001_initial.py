# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import dash.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout')),
                ('placeholder_uid', models.CharField(max_length=255, verbose_name='Placeholder')),
                ('plugin_uid', models.CharField(max_length=255, verbose_name='Plugin name')),
                ('plugin_data', models.TextField(null=True, verbose_name='Plugin data', blank=True)),
                ('position', models.PositiveIntegerField(null=True, verbose_name='Position', blank=True)),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
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
                ('plugin_uid', models.CharField(verbose_name='Plugin UID', unique=True, max_length=255, editable=False)),
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
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('is_public', models.BooleanField(default=False, help_text='Makes your dashboard to be visible to the public. Visibility of workspaces could be adjust separately for each workspace, however setting your dashboard to be visible to public, makes your default workspace visible to public too.', verbose_name='Is public?')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, unique=True, on_delete=models.CASCADE)),
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
                ('layout_uid', models.CharField(max_length=25, verbose_name='Layout')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(verbose_name='Slug', unique=True, editable=False)),
                ('position', dash.fields.OrderField(null=True, verbose_name='Position', blank=True)),
                ('is_public', models.BooleanField(default=False, help_text='Makes your workspace to be visible to the public.', verbose_name='Is public?')),
                ('is_clonable', models.BooleanField(default=False, help_text='Makes your workspace to be cloneable by other users.', verbose_name='Is cloneable?')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Dashboard workspace',
                'verbose_name_plural': 'Dashboard workspaces',
            },
        ),
        migrations.AddField(
            model_name='dashboardentry',
            name='workspace',
            field=models.ForeignKey(verbose_name='Workspace', blank=True, to='dash.DashboardWorkspace', null=True, on_delete=models.CASCADE),
        ),
        migrations.AlterUniqueTogether(
            name='dashboardworkspace',
            unique_together=set([('user', 'slug'), ('user', 'name')]),
        ),
    ]
