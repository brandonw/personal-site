# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            ('pub_time', self.gf('django.db.models.fields.TimeField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=('pub_date',), max_length=50, populate_from='name')),
            ('post_text', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('post_text_markup_type', self.gf('django.db.models.fields.CharField')(default='markdown', max_length=30)),
            ('_post_text_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'PostTag'
        db.create_table(u'blog_posttag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'blog', ['PostTag'])

        # Adding model 'PostImage'
        db.create_table(u'blog_postimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['PostImage'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'PostTag'
        db.delete_table(u'blog_posttag')

        # Deleting model 'PostImage'
        db.delete_table(u'blog_postimage')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            '_post_text_rendered': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'post_text_markup_type': ('django.db.models.fields.CharField', [], {'default': "'markdown'", 'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'pub_time': ('django.db.models.fields.TimeField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('pub_date',)", 'max_length': '50', 'populate_from': "'name'"})
        },
        u'blog.postimage': {
            'Meta': {'object_name': 'PostImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"})
        },
        u'blog.posttag': {
            'Meta': {'object_name': 'PostTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['blog']