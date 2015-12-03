from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response(
        '2048.html',
        {},
        context_instance=RequestContext(request))
