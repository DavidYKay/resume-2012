# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platform'
        db.create_table('gigs_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('appstore_logo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('gigs', ['Platform'])

        # Adding model 'GigType'
        db.create_table('gigs_gigtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('gigs', ['GigType'])

        # Adding model 'Gig'
        db.create_table('gigs_gig', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.GigType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('begin_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('gigs', ['Gig'])

        # Adding M2M table for field platforms on 'Gig'
        db.create_table('gigs_gig_platforms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gig', models.ForeignKey(orm['gigs.gig'], null=False)),
            ('platform', models.ForeignKey(orm['gigs.platform'], null=False))
        ))
        db.create_unique('gigs_gig_platforms', ['gig_id', 'platform_id'])

        # Adding model 'Video'
        db.create_table('gigs_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gig', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.Gig'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('gigs', ['Video'])

        # Adding model 'Photo'
        db.create_table('gigs_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gig', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.Gig'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gigs', ['Photo'])

        # Adding model 'CodeRepo'
        db.create_table('gigs_coderepo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gig', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.Gig'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('gigs', ['CodeRepo'])

        # Adding model 'AppStoreListing'
        db.create_table('gigs_appstorelisting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gig', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.Gig'])),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gigs.Platform'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('gigs', ['AppStoreListing'])


    def backwards(self, orm):
        # Deleting model 'Platform'
        db.delete_table('gigs_platform')

        # Deleting model 'GigType'
        db.delete_table('gigs_gigtype')

        # Deleting model 'Gig'
        db.delete_table('gigs_gig')

        # Removing M2M table for field platforms on 'Gig'
        db.delete_table('gigs_gig_platforms')

        # Deleting model 'Video'
        db.delete_table('gigs_video')

        # Deleting model 'Photo'
        db.delete_table('gigs_photo')

        # Deleting model 'CodeRepo'
        db.delete_table('gigs_coderepo')

        # Deleting model 'AppStoreListing'
        db.delete_table('gigs_appstorelisting')


    models = {
        'gigs.appstorelisting': {
            'Meta': {'object_name': 'AppStoreListing'},
            'gig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.Gig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.Platform']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'gigs.coderepo': {
            'Meta': {'object_name': 'CodeRepo'},
            'gig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.Gig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'gigs.gig': {
            'Meta': {'ordering': "['-end_date', '-begin_date']", 'object_name': 'Gig'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gigs.Platform']", 'symmetrical': 'False', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.GigType']"})
        },
        'gigs.gigtype': {
            'Meta': {'object_name': 'GigType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gigs.photo': {
            'Meta': {'object_name': 'Photo'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'gig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.Gig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gigs.platform': {
            'Meta': {'object_name': 'Platform'},
            'appstore_logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gigs.video': {
            'Meta': {'object_name': 'Video'},
            'gig': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gigs.Gig']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gigs']