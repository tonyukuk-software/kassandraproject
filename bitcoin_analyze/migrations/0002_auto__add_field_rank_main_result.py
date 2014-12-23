# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rank.main_result'
        db.add_column(u'bitcoin_analyze_rank', 'main_result',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rank.main_result'
        db.delete_column(u'bitcoin_analyze_rank', 'main_result')


    models = {
        u'bitcoin_analyze.change': {
            'Meta': {'object_name': 'Change'},
            'change_value': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'bitcoin_analyze.change_rate': {
            'Meta': {'object_name': 'Change_Rate'},
            'change_rate_value': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'bitcoin_analyze.expected_value': {
            'Meta': {'object_name': 'Expected_Value'},
            'high': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'low': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'bitcoin_analyze.rank': {
            'Meta': {'object_name': 'Rank'},
            'change': ('django.db.models.fields.FloatField', [], {'default': '20.0'}),
            'change_rate': ('django.db.models.fields.FloatField', [], {'default': '20.0'}),
            'expected_value': ('django.db.models.fields.FloatField', [], {'default': '20.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'twitter': ('django.db.models.fields.FloatField', [], {'default': '20.0'}),
            'volume': ('django.db.models.fields.FloatField', [], {'default': '20.0'})
        },
        u'bitcoin_analyze.twitter': {
            'Meta': {'object_name': 'Twitter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'negative_tweet_number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'positive_tweet_number': ('django.db.models.fields.SmallIntegerField', [], {}),
            'processed_tweets_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '100'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'bitcoin_analyze.volume': {
            'Meta': {'object_name': 'Volume'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'volume_value': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['bitcoin_analyze']