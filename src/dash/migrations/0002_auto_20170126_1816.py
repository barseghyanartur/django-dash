# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import dash.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardsettings',
            name='allow_different_layouts',
            field=models.BooleanField(default=False, help_text='Allows you to use different layouts for each workspace.', verbose_name='Allow different layouts per workspace?'),
        ),
        migrations.AlterField(
            model_name='dashboardworkspace',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='Slug', slugify=dash.helpers.slugify_workspace),
        ),
    ]
