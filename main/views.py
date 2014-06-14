import datetime
from django.template import RequestContext,loader,Context
from main.forms import LoginForm,RegistrationFormUniqueEmail
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate

def home(request):
    # This view is missing all form handling logic for simplicity of the example
    grid_rows = []

    if "POST" == request.method:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    print "user is valid and active"
                else:
                    print "password is valid but account is disabled"
            else:
                print "username and password are incorrect"
    else:
        login_form = LoginForm()
        signup_form = RegistrationFormUniqueEmail()

    if 'GET' == request.method:
        t = loader.get_template('main.html')
        c = RequestContext(request,{'login_form': login_form, 'signup_form':signup_form})
        resp = t.render(c)

    return HttpResponse(resp)

