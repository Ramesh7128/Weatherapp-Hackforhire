import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'weather.settings'
import django
from django.utils import timezone
from daemonize import Daemonize
import urllib2
from django.core.management import setup_environ
from weather import settings
import json
from bs4 import BeautifulSoup
import json
from weatherapp.models import weatherreport


setup_environ(settings)


def weatherdetails():

    jsondata = open('state_city1.js')
    statescitylist = json.load(jsondata)
    print statescitylist
    for key, value in statescitylist.items():
        url = "http://api.openweathermap.org/data/2.5/forecast?q="+value[0]+"&cnt=10"
        languages = urllib2.urlopen(url)
        datalang = json.load(languages)
        for k, v in datalang.items():
            try:
                print key
                print
                print datalang['city']['name']
                date =







if __name__=="__main__":
    weatherdetails()
