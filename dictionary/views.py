from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import DictionaryForm
from django.core.urlresolvers import reverse
from .models import Word


class DictionaryView(View):
    form_class = DictionaryForm
    template_name = 'dictionary.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'dictionary.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # algo
            word = form.cleaned_data['word'].strip()
            words = Word.objects.filter(name=word)
            message = None
            if len(words) < 1:
                message = word + "  not found in our dictionary"
            return render(request, self.template_name, {'words': words,
                                                        'form': form,
                                                        'message': message
                                                        })

        return render(request, self.template_name, {'form': form})
