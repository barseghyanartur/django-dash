__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('BooleanRadioSelect',)

from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _

BOOLEAN_CHOICES = (
    (True, _("Yes")),
    (False, _("No"))
)

class BooleanRadioSelect(RadioSelect):
    """
    Boolean radio select for Django.

    :example:
    
    >>> class DummyForm(forms.Form):
    >>>     agree = forms.BooleanField(label=_("Agree?"), required=False, widget=BooleanRadioSelect)
    """
    def __init__(self, *args, **kwargs):
        # Override the default renderer if we were passed one.
        renderer = kwargs.pop('renderer', None)
        if renderer:
            self.renderer = renderer

        if not 'choices' in kwargs:
            kwargs['choices'] = BOOLEAN_CHOICES

        super(BooleanRadioSelect, self).__init__(*args, **kwargs)
