import datetime
from time import struct_time

from django import template

__title__ = 'dash.contrib.plugins.rss_feed.templatetags.rss_feed_tags'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('convert_to_datetime',)

register = template.Library()


@register.filter
def convert_to_datetime(value):
    """Convert to datetime."""

    if isinstance(value, struct_time):
        converted = datetime.datetime(
            year=value.tm_year,
            month=value.tm_mon,
            day=value.tm_mday,
            hour=value.tm_hour,
            minute=value.tm_min,
            second=value.tm_sec
        )
    else:
        converted = value
    return converted
