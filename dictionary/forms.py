from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Div
from crispy_forms.bootstrap import FormActions
import autocomplete_light


class DictionaryForm(forms.Form):
    word = forms.CharField(
        max_length=200,
        label='',
        widget=autocomplete_light.TextWidget('WordAutocomplete'),
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form_size'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(Div(Div('word',
                                            css_class='col-lg-3'),
                                        Div(Submit('Submit',
                                                   'Know Meaning',
                                                   css_class="btn-primary"),
                                            css_class='col-lg-9'),
                                        css_class='row-fluid'))
        super(DictionaryForm, self).__init__(*args, **kwargs)
