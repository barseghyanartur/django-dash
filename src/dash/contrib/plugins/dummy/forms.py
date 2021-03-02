import logging

from django import forms
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _

from transliterate.contrib.apps.translipsum import TranslipsumGenerator
from transliterate.contrib.apps.translipsum.utils import Generator

from ....base import DashboardPluginFormBase
from ....settings import DEBUG
from ....widgets import BooleanRadioSelect
from .defaults import (
    DEFAULT_MAX_CHARS,
    LANGUAGE_CHOICES,
    LANGUAGE_CHOICES_KEYS,
)

__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = ('DummyForm', 'DummyShortcutsForm')

logger = logging.getLogger(__name__)


class DummyForm(forms.Form, DashboardPluginFormBase):
    """Dummy form (for main `placeholder`)."""

    plugin_data_fields = [
        ("show_title", False),
        ("generate_lipsum", False),
        ("lipsum_language", ""),
        ("lipsum_max_chars", DEFAULT_MAX_CHARS),
        ("text", "")
    ]
    show_title = forms.BooleanField(label=_("Show title?"),
                                    required=False,
                                    initial=False,
                                    widget=BooleanRadioSelect)
    generate_lipsum = forms.BooleanField(label=_("Generate lorem ipsum?"),
                                         required=False,
                                         initial=False,
                                         widget=BooleanRadioSelect)
    lipsum_language = forms.ChoiceField(label=_("Language"),
                                        required=False,
                                        choices=LANGUAGE_CHOICES)
    lipsum_max_chars = forms.IntegerField(label=_("Max number of chars for "
                                                  "generated text"),
                                          required=True,
                                          initial=DEFAULT_MAX_CHARS)
    text = forms.CharField(label=_("Generated lorem ipsum text"),
                           required=False,
                           widget=forms.widgets.HiddenInput)

    def save_plugin_data(self, request=None):
        """Save plugin data.

        We want to save the generated lorem ipsum text for later use.
        Thus, although we don't show it to the user, in case when
        ``generate_lipsum`` field is set to True, we silently generate the
        text and save it into the plugin data.
        """
        if self.cleaned_data.get('generate_lipsum', None):
            lipsum_language = self.cleaned_data.get('lipsum_language', None)
            try:
                if lipsum_language in LANGUAGE_CHOICES_KEYS:
                    if lipsum_language == 'en':
                        gen = Generator()
                    else:
                        gen = TranslipsumGenerator(
                            language_code=lipsum_language
                        )
                    text = gen.generate_paragraph()
                    truncator = Truncator(text)
                    self.cleaned_data['text'] = truncator.chars(
                        self.cleaned_data.get('lipsum_max_chars',
                                              DEFAULT_MAX_CHARS)
                    )
            except Exception as err:
                if DEBUG:
                    logger.debug(err)


class DummyShortcutsForm(DummyForm):
    """Dummy form for `shortucts` placeholder."""
