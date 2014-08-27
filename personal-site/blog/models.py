from django.db import models
from os.path import splitext, join
from autoslug import AutoSlugField
from markupfield.fields import MarkupField

def get_image_name(post_image, original_name):
    extension = splitext(original_name)
    return join(post_image.post.slug, post_image.name + extension[1])

class PostGroup:
    def __init__(self, year, month, posts):
        self.year = year
        self.month = month
        self.posts = posts

class PostManager(models.Manager):
    def grouped_by_date(self):
        dates = Post.objects.dates('pub_date', 'month', order='DESC')
        groups = [PostGroup(date.year, date.strftime('%B'),
            Post.objects.filter(pub_date__year=date.year)
                        .filter(pub_date__month=date.month)) for date in dates]
        return groups

class Post(models.Model):

    objects = PostManager()

    # post timestamp
    pub_date = models.DateField()
    pub_time = models.TimeField()

    # display post to the public
    is_published = models.BooleanField()

    # name of post
    name = models.CharField(max_length=100)

    # slug for post, unique per day
    slug = AutoSlugField(populate_from='name', unique_with='pub_date')

    # text of the post, rendered to template as markdown
    post_text = MarkupField(markup_type='markdown')

class PostTag(models.Model):

    post = models.ForeignKey(Post)

    # a tag the post is described by
    # TODO: ensure tag is composed of [\w-]+
    tag = models.CharField(max_length=25)

class PostImage(models.Model):

    post = models.ForeignKey(Post)

    # the name to refer to the image by
    name = models.CharField(max_length=25)

    # an image, to be used in post_text of the related post
    # easiest way to us an image uploaded via this model is to
    # grab the raw url in the media directory, and link to it
    # via a standard <img /> element
    image = models.ImageField(upload_to=get_image_name)
