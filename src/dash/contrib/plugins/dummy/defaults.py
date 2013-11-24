__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

LANGUAGE_CHOICES = (
    ('en', 'English'),
    ('hy', 'Armenian'),
    ('ka', 'Georgian'),
    ('el', 'Greek'),
    ('ru', 'Russian')
)

LANGUAGE_CHOICES_KEYS = [l[0] for l in LANGUAGE_CHOICES]

DEFAULT_MAX_CHARS = 40
