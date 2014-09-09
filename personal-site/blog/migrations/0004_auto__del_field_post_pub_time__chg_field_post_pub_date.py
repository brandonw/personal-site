# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.pub_time'
        db.delete_column(u'blog_post', 'pub_time')


        # Changing field 'Post.pub_date'
        db.alter_column(u'blog_post', 'pub_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Adding field 'Post.pub_time'
        db.add_column(u'blog_post', 'pub_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2014, 9, 7, 0, 0)),
                      keep_default=False)


        # Changing field 'Post.pub_date'
        db.alter_column(u'blog_post', 'pub_date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            '_post_text_rendered': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'post_text_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'blog.postimage': {
            'Meta': {'object_name': 'PostImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"})
        }
    }

    complete_apps = ['blog']