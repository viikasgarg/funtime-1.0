from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Reset, MultiField, Column, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FormActions
import datetime


class GridForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.grid_name = kwargs.pop('grid_name', "default")
        self.rows = kwargs.pop('rows', 1)
        self.cols = kwargs.pop('cols', 1)
        data = kwargs.pop('initial_data', None)
        readonly = kwargs.pop('readonly', False)
        super(GridForm, self).__init__(*args, **kwargs)
        form_rows = []
        for i in xrange(0, self.rows):
            form_row = []
            for j in xrange(0, self.cols):
                field_name = '%s_input_%s_%s' % (self.grid_name, i, j)
                self.fields[field_name] = forms.CharField(label="",
                                                          max_length=1,
                                                          required=False)
                if readonly:
                    self.fields[field_name].widget.attrs['readonly'] = readonly

                if data:
                    try:
                        if data[i][j] != 0:
                            print data[i][j]
                            self.fields[field_name].initial = data[i][j]
                    except:
                        pass

                form_row.append(
                    Div(field_name, css_class="col-md-1 square_field"))
            form_rows.append(Row(*form_row))

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.error_text_inline = False
        self.helper.layout = Layout(*form_rows)

    def clean(self):
        cleaned_data = self.cleaned_data
        data = []
        entered_value = 0
        for i in xrange(0, self.rows):
            row_data = []
            for j in xrange(0, self.cols):
                try:
                    value = cleaned_data.get(
                        '%s_input_%s_%s' % (
                          self.grid_name, i, j))
                    if value != '':
                        value = int(value)
                        if value not in range(1, 10):
                            raise ValueError
                        else:
                            entered_value += 1
                            row_data.append(value)
                    else:
                        row_data.append(0)
                except ValueError:
                    raise forms.ValidationError(
                        "Only Integer Values in range 1,9 allowed ")
            data.append(row_data)

        if entered_value < 16:
            raise forms.ValidationError("Please fill atleast 16 Fields ")

        return data
