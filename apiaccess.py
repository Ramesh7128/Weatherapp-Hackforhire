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
        l = ""
        for k, v in datalang.items():
            if k=="list":
                j = 0
                for i in v:
                    try:
                        d = datalang['list'][j]['dt_txt']
                        d = d[0:-9]
                        if l!=d:
                            weatherreport.objects.create(state=key,city=datalang['city']['name'],date=d,condition=datalang['list'][j]['weather'][0]['description'],temperature=int(datalang['list'][j]['main']['temp_max']))
                            l = d

                        j+= 1
                    except:
                        pass


if __name__=="__main__":
    weatherdetails()
