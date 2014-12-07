from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from weatherapp.models import weatherreport
from django.shortcuts import redirect
from django import forms
from datetime import datetime, timedelta

class FilterForm(forms.Form):
    location = forms.CharField(max_length=50,)
    noofdays = forms.IntegerField(help_text="1-5")
    condition = forms.CharField(max_length=50,help_text="cloudy,clear,overcast,rain")


def index(request):
    context = RequestContext(request)
    message = "weatherapp"
    context_dict = {}
    if request.method == 'POST':

        form = FilterForm(request.POST)

        if form.is_valid():
            location = request.POST['location']
            noofdays = request.POST['fromdate']
            condition = request.POST['condition']
            now = datetime.now()

            if location and noofdays and condition:
                dates = now+timedelta(days=noofdays)
                locationlist = weatherreport.objects.filter(location=location, condition__icontains=condition,date_range=(now,dates))

            elif location and noofdays:
                dates = now+timedelta(days=noofdays)
                locationlist = weatherreport.objects.filter(location=location, date_range=(now,dates))

            elif location and condition:
                locationlist = weatherreport.objects.filter(location=location, condition__icontains=condition)

            elif condition and noofdays:
                dates = now+timedelta(days=noofdays)
                locationlist = weatherreport.objects.filter(date_range=(now,dates),condition__icontains=condition)

            elif condition:
                locationlist = weatherreport.objects.filter(condition__icontains=condition)
            elif location:
                locationlist = weatherreport.objects.filter(location=location)

            else:
                locationlist = weatherreport.objects.filter(date_range=(now,dates))


            context_dict['locationlist'] = locationlist
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilterForm()
    context_dict['form'] = form

    return render_to_response('weatherapp/base.html', context_dict, context)



