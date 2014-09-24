# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import sorl.thumbnail.fields
import projects.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.PositiveSmallIntegerField(help_text=b'Projects will be ordered by this value.', unique=True)),
                ('name', models.CharField(help_text=b'The name of the project.', max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('link', models.URLField(help_text=b'An optional URL to the project.', blank=True)),
                ('short_descr', models.TextField(help_text=b'A short description displayed in the project index. This will be html escaped, so ensure it is plain text.')),
                ('full_descr', models.TextField(help_text=b'The full description of the project, in Markdown format. The value of this field  will not be html escaped.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(help_text=b'An image that should showcase what the project is or does.', upload_to=projects.models.get_slug)),
                ('project', models.ForeignKey(help_text=b'The project this image is related to.', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
