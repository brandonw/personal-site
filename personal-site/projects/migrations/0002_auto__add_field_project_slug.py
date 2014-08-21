# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.slug'
        db.add_column(u'projects_project', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=datetime.datetime(2014, 8, 20, 0, 0), unique=True, max_length=50, populate_from='name', unique_with=()),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.slug'
        db.delete_column(u'projects_project', 'slug')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'full_descr': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'short_descr': ('django.db.models.fields.TextField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']