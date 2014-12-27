# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bitcoin_Process'
        db.create_table(u'kassandraproject_bitcoin_process', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bitcoin', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('purchase_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('purchase_amount', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('sales_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('sales_amount', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'kassandraproject', ['Bitcoin_Process'])


    def backwards(self, orm):
        # Deleting model 'Bitcoin_Process'
        db.delete_table(u'kassandraproject_bitcoin_process')


    models = {
        u'kassandraproject.bitcoin_process': {
            'Meta': {'object_name': 'Bitcoin_Process'},
            'bitcoin': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_amount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'purchase_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sales_amount': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'sales_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['kassandraproject']