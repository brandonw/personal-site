# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project._full_descr_rendered'
        db.delete_column(u'projects_project', '_full_descr_rendered')

        # Deleting field 'Project.full_descr_markup_type'
        db.delete_column(u'projects_project', 'full_descr_markup_type')


        # Changing field 'Project.full_descr'
        db.alter_column(u'projects_project', 'full_descr', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Project._full_descr_rendered'
        db.add_column(u'projects_project', '_full_descr_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Project.full_descr_markup_type'
        db.add_column(u'projects_project', 'full_descr_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30),
                      keep_default=False)


        # Changing field 'Project.full_descr'
        db.alter_column(u'projects_project', 'full_descr', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'full_descr': ('django.db.models.fields.TextField', [], {}),
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