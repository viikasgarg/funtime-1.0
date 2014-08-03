import autocomplete_light

from .models import Word

# But you can make your subclass yourself and override methods.
class WordAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    def choices_for_request(self):
        """ Return choices for a particular request """
        return set([str(f) for f in super(WordAutocomplete, self).choices_for_request()])

autocomplete_light.register(Word, WordAutocomplete, search_fields=('name',),
    autocomplete_js_attributes={'placeholder': 'Seach Word ..',
    'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
    },
    )