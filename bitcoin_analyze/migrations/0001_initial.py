# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rank'
        db.create_table(u'bitcoin_analyze_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('twitter', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('expected_value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('volume', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('change', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('change_rate', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Rank'])

        # Adding model 'Twitter'
        db.create_table(u'bitcoin_analyze_twitter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processed_tweets_number', self.gf('django.db.models.fields.SmallIntegerField')(default=100)),
            ('positive_tweet_number', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('negative_tweet_number', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('result', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Twitter'])

        # Adding model 'Expected_Value'
        db.create_table(u'bitcoin_analyze_expected_value', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('high', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('low', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('last', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('result', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Expected_Value'])

        # Adding model 'Volume'
        db.create_table(u'bitcoin_analyze_volume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volume_value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('result', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Volume'])

        # Adding model 'Change'
        db.create_table(u'bitcoin_analyze_change', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('change_value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('result', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Change'])

        # Adding model 'Change_Rate'
        db.create_table(u'bitcoin_analyze_change_rate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('change_rate_value', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('result', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'bitcoin_analyze', ['Change_Rate'])


    def backwards(self, orm):
        # Deleting model 'Rank'
        db.delete_table(u'bitcoin_analyze_rank')

        # Deleting model 'Twitter'
        db.delete_table(u'bitcoin_analyze_twitter')

        # Deleting model 'Expected_Value'
        db.delete_table(u'bitcoin_analyze_expected_value')

        # Deleting model 'Volume'
        db.delete_table(u'bitcoin_analyze_volume')

        # Deleting model 'Change'
        db.delete_table(u'bitcoin_analyze_change')

        # Deleting model 'Change_Rate'
        db.delete_table(u'bitcoin_analyze_change_rate')


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
            'change': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'change_rate': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'expected_value': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitter': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'volume': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
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