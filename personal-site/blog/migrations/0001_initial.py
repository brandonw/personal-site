# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import blog.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(help_text=b'The date and time the post was published.', verbose_name=b'Publish Date')),
                ('is_published', models.BooleanField(help_text=b'Whether or not to make the post visible to visitors.')),
                ('name', models.CharField(help_text=b'A quick summary of the post.', max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('post_text', models.TextField(help_text=b'The content of the post, in Markdown format. The value of this field will not be html escaped.')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text=b'The tags to categorize this post by.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b"The name to use when linking to this image. The name  will be used in addition to the post's slug as the absolute url.", max_length=25)),
                ('image', models.ImageField(help_text=b"An image that will be linked to in the post's content. +To use this image in a post, upload the image via the admin interface, and then copy paste the absolute URL linked therein.", upload_to=blog.models.get_image_name)),
                ('post', models.ForeignKey(help_text=b'The post this image is related to.', to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
