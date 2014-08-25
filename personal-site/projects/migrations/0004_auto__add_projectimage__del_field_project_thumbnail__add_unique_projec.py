# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectImage'
        db.create_table(u'projects_projectimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'projects', ['ProjectImage'])

        # Deleting field 'Project.thumbnail'
        db.delete_column(u'projects_project', 'thumbnail')

        # Adding unique constraint on 'Project', fields ['priority']
        db.create_unique(u'projects_project', ['priority'])


    def backwards(self, orm):
        # Removing unique constraint on 'Project', fields ['priority']
        db.delete_unique(u'projects_project', ['priority'])

        # Deleting model 'ProjectImage'
        db.delete_table(u'projects_projectimage')

        # Adding field 'Project.thumbnail'
        db.add_column(u'projects_project', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            '_full_descr_rendered': ('django.db.models.fields.TextField', [], {}),
            'full_descr': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'full_descr_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'}),
            'short_descr': ('django.db.models.fields.TextField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'})
        },
        u'projects.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"})
        }
    }

    complete_apps = ['projects']