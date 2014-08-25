from django.db import models
from os.path import splitext
from autoslug import AutoSlugField
from markupfield.fields import MarkupField
from sorl.thumbnail import ImageField

def get_slug(project_image, original_name):
    extension = splitext(original_name)
    return str(project_image.project.slug) + extension[1]

class Project(models.Model):

    # affects ordering of the projects
    priority = models.PositiveSmallIntegerField(unique=True)

    # a clear name to identify what a project is
    name = models.CharField(max_length=50)

    # unique slug, based off of name
    slug = AutoSlugField(populate_from='name', unique=True)

    # a link to the repository, if open sourced
    link = models.URLField(blank=True)

    # a brief description of what the project is, in plain text format
    short_descr = models.TextField()

    # an in-depth description of what the project is, in Markdown format
    full_descr = MarkupField(markup_type='markdown')

class ProjectImage(models.Model):

    project = models.ForeignKey(Project)

    image = ImageField(upload_to=get_slug)
