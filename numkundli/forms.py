from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row
from crispy_forms.bootstrap import FormActions


class KundliForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)
    birthday = forms.DateField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row('first_name', 'middle_name', 'last_name', 'birthday'),
            FormActions(
                Submit('Submit', 'Know Your Future', css_class="btn-primary"),
            )
        )
        super(KundliForm, self).__init__(*args, **kwargs)
