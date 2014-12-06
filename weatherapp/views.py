from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from weatherapp.models import weatherreport
from django.shortcuts import redirect


def index(request):
    context = RequestContext(request)
    message = "weatherapp"
    context_dict = {}
    context_dict['message'] = message

    return render_to_response('weatherapp/base.html', context_dict, context)



