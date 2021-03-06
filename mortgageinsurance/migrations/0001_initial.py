# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Monthly'
        db.create_table(u'mortgageinsurance_monthly', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('insurer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('min_ltv', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('max_ltv', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('min_fico', self.gf('django.db.models.fields.IntegerField')()),
            ('max_fico', self.gf('django.db.models.fields.IntegerField')()),
            ('loan_term', self.gf('django.db.models.fields.IntegerField')()),
            ('pmt_type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('min_loan_amt', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('max_loan_amt', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('premium', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal(u'mortgageinsurance', ['Monthly'])

        # Adding model 'Upfront'
        db.create_table(u'mortgageinsurance_upfront', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('loan_type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('va_status', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('va_first_use', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('min_ltv', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('max_ltv', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('premium', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal(u'mortgageinsurance', ['Upfront'])


    def backwards(self, orm):
        # Deleting model 'Monthly'
        db.delete_table(u'mortgageinsurance_monthly')

        # Deleting model 'Upfront'
        db.delete_table(u'mortgageinsurance_upfront')


    models = {
        u'mortgageinsurance.monthly': {
            'Meta': {'object_name': 'Monthly'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'loan_term': ('django.db.models.fields.IntegerField', [], {}),
            'max_fico': ('django.db.models.fields.IntegerField', [], {}),
            'max_loan_amt': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'max_ltv': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'min_fico': ('django.db.models.fields.IntegerField', [], {}),
            'min_loan_amt': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'min_ltv': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'pmt_type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'premium': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'})
        },
        u'mortgageinsurance.upfront': {
            'Meta': {'object_name': 'Upfront'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan_type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'max_ltv': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'min_ltv': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'premium': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'va_first_use': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'va_status': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['mortgageinsurance']