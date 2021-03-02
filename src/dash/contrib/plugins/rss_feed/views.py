import logging

from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import feedparser

from ....settings import DEBUG

from .defaults import (
    DEFAULT_MAX_FEED_ITEMS,
    DEFAULT_SHOW_TITLE,
    DEFAULT_TRUNCATE_AFTER,
)
from .forms import ReadRSSFeedForm
from .helpers import max_num_template


__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('get_feed',)

logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
@login_required
def get_feed(request,
             layout_uid,
             placeholder_uid,
             plugin_uid,
             template_name='rss_feed/get_feed.html',
             template_name_ajax='rss_feed/get_feed_ajax.html'):
    """Get feed.

    :param django.http.HttpRequest request:
    :param str layout_uid:
    :param str placeholder_uid:
    :param str plugin_uid:
    :param str template_name:
    :param str template_name_ajax:
    :return django.http.HttpResponse:
    """
    form = ReadRSSFeedForm(request.POST)

    context = {}

    if form.is_valid():

        feed_url = form.cleaned_data.get('feed_url')
        custom_feed_title = form.cleaned_data.get('custom_feed_title', None)
        show_feed_title = form.cleaned_data.get('show_feed_title',
                                                DEFAULT_SHOW_TITLE)
        max_items = form.cleaned_data.get('max_items')
        truncate_after = form.cleaned_data.get('truncate_after',
                                               DEFAULT_TRUNCATE_AFTER)
        cache_for = form.cleaned_data.get('cache_for')

        key = '{0}-{1}-{2}-{3}'.format(layout_uid,
                                       placeholder_uid,
                                       plugin_uid,
                                       feed_url)
        feed = cache.get(key)

        if not feed:

            try:
                validate = URLValidator()
                valid_url = False
                try:
                    validate(feed_url)
                    valid_url = True
                except ValidationError as err:
                    valid_url = False
                    if DEBUG:
                        logger.debug(err)

                # Reading the feed and sending results to the template
                if valid_url:
                    # Saving raw data in case someone wants to show things
                    # differently.
                    feed = feedparser.parse(feed_url)
                    cache.set(key, feed, int(cache_for))

            except Exception as err:
                if DEBUG:
                    logger.debug(err)

        context = {
            'feed': feed,
            'custom_feed_title': custom_feed_title,
            'show_feed_title': show_feed_title,
            'truncate_after': truncate_after,
            'max_feed_items': max_num_template(max_items,
                                               DEFAULT_MAX_FEED_ITEMS)
        }

    if request.is_ajax():
        template_name = template_name_ajax

    return render(request, template_name, context)
