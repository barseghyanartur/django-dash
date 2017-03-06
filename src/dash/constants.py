from django.utils.translation import ugettext_lazy as _

__title__ = 'dash.constants'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
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
