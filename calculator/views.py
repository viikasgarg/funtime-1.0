# Create your views here.
from django.template import RequestContext,loader,Context
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('calculator.html',
                              context_instance = RequestContext(request))
