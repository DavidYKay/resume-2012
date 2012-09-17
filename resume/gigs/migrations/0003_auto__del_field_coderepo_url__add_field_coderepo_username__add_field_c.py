# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CodeRepo.url'
        db.delete_column('gigs_coderepo', 'url')

        # Adding field 'CodeRepo.username'
        db.add_column('gigs_coderepo', 'username',
                      self.gf('django.db.models.fields.CharField')(default='DavidYKay', max_length=100),
                      keep_default=False)

        # Adding field 'CodeRepo.reponame'
        db.add_column('gigs_coderepo', 'reponame',
                      self.gf('django.db.models.fields.CharField')(default='QUADRO', max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CodeRepo.url'
        raise RuntimeError("Cannot reverse this migration. 'CodeRepo.url' and its values cannot be restored.")
        # Deleting field 'CodeRepo.username'
        db.delete_column('gigs_coderepo', 'username')

        # Deleting field 'CodeRepo.reponame'
        db.delete_column('gigs_coderepo', 'reponame')


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
            'reponame': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gigs.externalsite': {
            'Meta': {'ordering': "['order']", 'object_name': 'ExternalSite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
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