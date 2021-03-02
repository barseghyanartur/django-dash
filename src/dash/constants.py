from django.utils.translation import gettext_lazy as _

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'ACTION_CHOICE_APPEND',
    'ACTION_CHOICE_REPLACE',
    'ACTION_CHOICES',
)


ACTION_CHOICE_REPLACE = '1'
ACTION_CHOICE_APPEND = '2'
ACTION_CHOICES = (
    (ACTION_CHOICE_APPEND, _("Append")),
    (ACTION_CHOICE_REPLACE, _("Replace")),
)
