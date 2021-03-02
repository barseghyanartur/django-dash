import datetime
from time import struct_time

from django import template

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
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
