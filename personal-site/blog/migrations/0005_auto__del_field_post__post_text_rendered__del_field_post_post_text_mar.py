# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post._post_text_rendered'
        db.delete_column(u'blog_post', '_post_text_rendered')

        # Deleting field 'Post.post_text_markup_type'
        db.delete_column(u'blog_post', 'post_text_markup_type')


        # Changing field 'Post.post_text'
        db.alter_column(u'blog_post', 'post_text', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Post._post_text_rendered'
        db.add_column(u'blog_post', '_post_text_rendered',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Post.post_text_markup_type'
        db.add_column(u'blog_post', 'post_text_markup_type',
                      self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30),
                      keep_default=False)


        # Changing field 'Post.post_text'
        db.alter_column(u'blog_post', 'post_text', self.gf('markupfield.fields.MarkupField')(rendered_field=True))

    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_text': ('django.db.models.fields.TextField', [], {}),
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