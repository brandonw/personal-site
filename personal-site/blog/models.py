from django.db import models
from os.path import splitext, join

from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from taggit.models import TaggedItem, Tag
from markdown import markdown
from misc.code_blocks_preprocessor import CodeBlockExtension

def get_image_name(post_image, original_name):
    extension = splitext(original_name)
    return join(post_image.post.slug + '-', post_image.name + extension[1])

class Post(models.Model):

    # post timestamp
    pub_date = models.DateTimeField(verbose_name='Publish Date',
        help_text='The date and time the post was published.')

    # display post to the public
    is_published = models.BooleanField(default=False,
        help_text='Whether or not to make the post visible to visitors.')

    # name of post
    name = models.CharField(max_length=100,
        help_text='A quick summary of the post.')

    # slug for post, unique per day
    slug = AutoSlugField(populate_from='name')

    # text of the post, rendered to template as markdown
    post_text = models.TextField(
        help_text='The content of the post, in Markdown format. The value ' +
        'of this field will not be html escaped.')

    # tags attached to this post
    # note that currently, tags are displayed regardless of whether or not
    # the post is published. to prevent tags from being displayed, do not
    # assign a post any tags until it is published.
    # alternatively, create a new template tag that filters the posts
    # before returning the tags
    tags = TaggableManager(help_text='The tags to categorize this post by.')

    def get_preview(self):
        (before, sep, after) = self.post_text.partition('<!--break-->')
        if sep == '':
            return ''
        return markdown(before, extensions=[CodeBlockExtension()])

    def get_full(self):
        return markdown(self.post_text, extensions=[CodeBlockExtension()])

    def __unicode__(self):
        if self.is_published:
            return self.name
        else:
            return self.name + '- not published'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog-post',
                kwargs={'year': self.pub_date.year,
                        'month': self.pub_date.month,
                        'day': self.pub_date.day,
                        'slug': self.slug})

class PostImage(models.Model):

    post = models.ForeignKey(Post,
        help_text='The post this image is related to.')

    # the name to refer to the image by
    name = models.CharField(max_length=25,
        help_text='The name to use when linking to this image. The name ' +
        ' will be used in addition to the post\'s slug as the absolute url.')

    # an image, to be used in post_text of the related post
    image = models.ImageField(upload_to=get_image_name,
        help_text='An image that will be linked to in the post\'s content. +'
        'To use this image in a post, upload the image via the admin ' +
        'interface, and then copy paste the absolute URL linked therein.')

    def __unicode__(self):
        return self.post.name

    def get_absolute_url(self):
        return self.image.url
