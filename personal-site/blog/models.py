from django.db import models
from os.path import splitext, join

from autoslug import AutoSlugField
from markupfield.fields import MarkupField
from taggit.managers import TaggableManager

def get_image_name(post_image, original_name):
    extension = splitext(original_name)
    return join(post_image.post.slug + '-', post_image.name + extension[1])

class PostGroup:
    def __init__(self, year, month, posts):
        self.year = year
        self.month = month
        self.posts = posts

class PostManager(models.Manager):
    def group_by_date(self, show_unpublished=False):
        objects = Post.objects
        if not show_unpublished:
            objects = objects.filter(is_published__exact=True)

        dates = objects.datetimes('pub_date', 'month', order='DESC')
        groups = [PostGroup(date.year, date.strftime('%B'),
            objects.filter(pub_date__year=date.year)
                   .filter(pub_date__month=date.month)
                   .order_by('-pub_date')) for date in dates]
        return groups

class Post(models.Model):

    objects = PostManager()

    # post timestamp
    pub_date = models.DateTimeField(verbose_name='Publish Date',
        help_text='The date and time the post was published.')

    # display post to the public
    is_published = models.BooleanField(
        help_text='Whether or not to make the post visible to visitors.')

    # name of post
    name = models.CharField(max_length=100,
        help_text='A quick summary of the post.')

    # slug for post, unique per day
    slug = AutoSlugField(populate_from='name')

    # text of the post, rendered to template as markdown
    post_text = MarkupField(markup_type='markdown',
        help_text='The content of the post, in Markdown format. The value ' +
        'of this field will not be html escaped.')

    # tags attached to this post
    # note that currently, tags are displayed regardless of whether or not
    # the post is published. to prevent tags from being displayed, do not
    # assign a post any tags until it is published.
    # alternatively, create a new template tag that filters the posts
    # before returning the tags
    tags = TaggableManager(help_text='The tags to categorize this post by.')

    def __unicode__(self):
        return self.name

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
