from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from weatherapp.models import weatherreport
from django.shortcuts import redirect
from django import forms
from datetime import datetime, timedelta

class FilterForm(forms.Form):
    location = forms.CharField(max_length=50,required=False)
    noofdays = forms.IntegerField(help_text="range :1-5 days",required=False)
    condition = forms.CharField(max_length=50,help_text="cloudy,clear,overcast,rain",required=False)


def index(request):
    context = RequestContext(request)
    message = "weatherapp"
    context_dict = {}
    if request.method == 'POST':

        form = FilterForm(request.POST)
        location = request.POST['location']
        noofdays = request.POST['noofdays']
        condition = request.POST['condition']
        now = datetime.now()

        if location and noofdays and condition:
            dates = now+timedelta(days=str(noofdays))
            locationlist = weatherreport.objects.filter(city__icontains=location, condition__icontains=condition)

        elif location and noofdays:
            dates = now+timedelta(days=str(noofdays))
            locationlist = weatherreport.objects.filter(city__icontains=location)

        elif location and condition:
            locationlist = weatherreport.objects.filter(city__icontains=location, condition__icontains=condition)

        elif condition and noofdays:
            dates = now+timedelta(days=str(noofdays))
            locationlist = weatherreport.objects.filter(condition__icontains=condition)

        elif condition:
            locationlist = weatherreport.objects.filter(condition__icontains=condition)
        elif location:
            locationlist = weatherreport.objects.filter(city__icontains=location)

        else:
            locationlist = weatherreport.objects.all()

        noofdays = int(noofdays)
        # if noofdays:
        #     newlist = []
        #     cityname=""
        #     for lolist in locationlist:
        #        newlist=weatherreport()
        #        if noofdays and cityname!=lolist.city:
        #            newlist = lolist
        #            cityname = lolist.city
        #            noofdays = noofdays-1





        context_dict['locationlist'] = locationlist
        context_dict['noofdays'] = noofdays
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilterForm()
    context_dict['form'] = form

    return render_to_response('weatherapp/base.html', context_dict, context)



