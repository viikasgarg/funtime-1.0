from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import KundliForm
from django.core.urlresolvers import reverse
from .algo import NumKundliInfo
'''
def home(request):
    error = False
    context = {'error':error}
    return render_to_response('home.html', context)

def know(request):
    error = False

    if 'firstname' in request.GET:
        firstname = request.GET['firstname']

    if not firstname or len(firstname) ==0 :
        error = True

    if 'middlename' in request.GET:
        middlename = request.GET['middlename']

    if 'lastname' in request.GET:
        lastname = request.GET['lastname']

    if not lastname or len(lastname) ==0 :
        error = True

    if 'date' in request.GET:
        date = request.GET['date']

    if not date or len(date) ==0 :
        error = True

    if error == False:
        return render_to_response('know.html',
                {'error': error})
    return render_to_response('home.html',
        {'error': error})

'''


class KundliFormView(View):
    form_class = KundliForm
    template_name = 'numkundli.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'numkundli.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # algo
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            birthday = form.cleaned_data['birthday']
            info = NumKundliInfo(birthday, first_name, middle_name, last_name)
            title = first_name + " " + middle_name + " " + last_name + \
                " [ " + birthday.strftime("%d %B %Y (%A)") + " ]"

            return render(request, 'info.html', {'info': info, 'title': title})

        return render(request, self.template_name, {'form': form})
