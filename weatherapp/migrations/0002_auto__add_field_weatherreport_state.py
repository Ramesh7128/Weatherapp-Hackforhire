# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'weatherreport.state'
        db.add_column(u'weatherapp_weatherreport', 'state',
                      self.gf('django.db.models.fields.CharField')(default='null', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'weatherreport.state'
        db.delete_column(u'weatherapp_weatherreport', 'state')


    models = {
        u'weatherapp.weatherreport': {
            'Meta': {'object_name': 'weatherreport'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['weatherapp']