__title__ = 'dash.contrib.plugins.dummy.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DEFAULT_MAX_CHARS',
    'LANGUAGE_CHOICES',
    'LANGUAGE_CHOICES_KEYS',
)

LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('hy', 'Armenian'),
    ('ka', 'Georgian'),
    ('el', 'Greek'),
    ('ru', 'Russian')
)

LANGUAGE_CHOICES_KEYS = [__val[0] for __val in LANGUAGE_CHOICES]

DEFAULT_MAX_CHARS = 40
