from django.db import models
from os.path import splitext
from autoslug import AutoSlugField
from markupfield.fields import MarkupField

def project_filename(project, original_name):
    extension = splitext(original_name)
    return str(project.slug) + extension[1]

class Project(models.Model):

    # affects ordering of the projects
    priority = models.PositiveSmallIntegerField()

    # a clear name to identify what a project is
    name = models.CharField(max_length=50)

    # unique slug, based off of name
    slug = AutoSlugField(populate_from='name', unique=True)

    # a single image used to give a preview of what the project looks like
    thumbnail = models.ImageField(upload_to=project_filename)

    # a link to the repository, if open sourced
    link = models.URLField(blank=True)

    # a brief description of what the project is, in plain text format
    short_descr = models.TextField()

    # an in-depth description of what the project is, in Markdown format
    full_descr = MarkupField(markup_type='markdown')

