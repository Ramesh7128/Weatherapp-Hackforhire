# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'weatherreport'
        db.create_table(u'weatherapp_weatherreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temperature', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'weatherapp', ['weatherreport'])


    def backwards(self, orm):
        # Deleting model 'weatherreport'
        db.delete_table(u'weatherapp_weatherreport')


    models = {
        u'weatherapp.weatherreport': {
            'Meta': {'object_name': 'weatherreport'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['weatherapp']