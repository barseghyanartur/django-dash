# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import slim.models
import datetime
import news.models
import tinymce.models
import slim.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', tinymce.models.HTMLField(verbose_name='Body')),
                ('image', models.ImageField(upload_to=news.models._news_images, null=True, verbose_name='Headline image', blank=True)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2016, 1, 23, 6, 40, 33, 487741), null=True, verbose_name='Date published', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('language', slim.models.fields.LanguageField(default=b'en', max_length=10, verbose_name='Language', choices=[(b'en', 'English'), (b'hy', b'Armenian'), (b'nl', 'Nederlands'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439')])),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created', null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', null=True)),
                ('translation_of', models.ForeignKey(related_name='translations', blank=True, to='news.NewsItem', help_text='Leave this empty for entries in the primary language.', null=True, verbose_name='Translation of')),
            ],
            options={
                'verbose_name': 'News item',
                'verbose_name_plural': 'News items',
            },
            bases=(models.Model, slim.models.Slim),
        ),
    ]
