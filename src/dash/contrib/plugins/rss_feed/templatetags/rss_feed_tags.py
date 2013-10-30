import datetime

from django import template

register = template.Library()

@register.filter
def convert_to_datetime(value):
    converted = datetime.datetime(
        year = value.tm_year,
        month = value.tm_mon,
        day = value.tm_mday,
        hour = value.tm_hour,
        minute = value.tm_min,
        second = value.tm_sec
    )
    return converted
