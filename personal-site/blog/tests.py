from django.test import TestCase
from django.utils import timezone
from users.models import User

from datetime import timedelta
from blog.models import get_image_name, Post, PostImage

# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        self.username = 'test'
        self.password = 'testpass'
        superuser = User.objects.create_superuser(
                self.username,
                'test@test.com',
                self.password)
        post1 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=2),
                is_published=True, name='Test post #1',
                post_text = '*test*<!--break-->rest')
        post1.tags.add('tag1', 'tag2')
        post2 = Post.objects.create(
                pub_date=timezone.now(),
                is_published=True, name='Test post #2',
                post_text = '*test*<!--break-->rest')
        post2.tags.add('tag3', 'tag4')
        post3 = Post.objects.create(
                pub_date=timezone.now() + timedelta(days=1),
                is_published=True, name='Test post #3',
                post_text = '*test*<!--break-->rest')
        post3.tags.add('tag1', 'tag4')
        post4 = Post.objects.create(
                pub_date=timezone.now() + timedelta(days=3),
                is_published=False, name='Test post #4',
                post_text = '*test*<!--break-->rest')
        post4.tags.add('unpub')
        post5 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #5',
                post_text = '*test*<!--break-->rest')
        post6 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #6',
                post_text = '*test*<!--break-->rest')
        post7 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #7',
                post_text = '*test*<!--break-->rest')
        post8 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #8',
                post_text = '*test*<!--break-->rest')
        post9 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #9',
                post_text = '*test*<!--break-->rest')
        post10 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #10',
                post_text = '*test*<!--break-->rest')
        post11 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #11',
                post_text = '*test*<!--break-->rest')
        post12 = Post.objects.create(
                pub_date=timezone.now() - timedelta(days=10),
                is_published=True, name='Test post #12',
                post_text = '*test*<!--break-->rest')
        postimg1 = PostImage.objects.create(post=post1, name='test-img',
                image='/tmp/foo/bar.jpg')
        postimg2 = PostImage.objects.create(post=post3, name='test-img-2',
                image='/tmp/foo/bar2.jpg')

    def test_get_image_name(self):
        post = Post.objects.get(name='Test post #1')
        img = post.postimage_set.first()
        self.assertEqual('test-post-1-test-img.jpg', get_image_name(img,
            'bar.jpg'))

    def test_blog_index(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 10)

        # make sure un-published posts are not visible
        for post in response.context['posts']:
            self.assertTrue(post.name != 'Test post #4')
        response = self.client.get('/blog/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)
        for post in response.context['posts']:
            self.assertTrue(post.name != 'Test post #4')

    def test_blog_feeds(self):
        response = self.client.get('/blog/rss/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/blog/atom/')
        self.assertEqual(response.status_code, 200)

    def test_tag(self):
        post = Post.objects.get(name='Test post #3')
        for tagslug in post.tags.slugs():
            response = self.client.get('/blog/tag/%s/' % (tagslug))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(response.context['taggedposts']) > 0)

    def test_post(self):
        post = Post.objects.get(name='Test post #3')
        self.assertEqual(post.get_preview(), '<p><em>test</em></p>')
        self.assertEqual(post.get_full(),
                '<p><em>test</em><!--break-->rest</p>')
        response = self.client.get('/blog/posts/%d/%d/%d/%s/' %
                (post.pub_date.year, post.pub_date.month, post.pub_date.day,
                post.slug))
        self.assertEqual(response.status_code, 200)

    def test_unpubbed_post(self):
        post = Post.objects.get(name='Test post #4')
        response = self.client.get('/blog/posts/%d/%d/%d/%s/' %
                (post.pub_date.year, post.pub_date.month, post.pub_date.day,
                post.slug))
        self.assertEqual(response.status_code, 404)

    def test_auth_blogpost(self):
        self.assertTrue(self.client.login(username=self.username,
            password=self.password))
        post = Post.objects.get(name='Test post #4')
        response = self.client.get('/blog/posts/%d/%d/%d/%s/' %
                (post.pub_date.year, post.pub_date.month, post.pub_date.day,
                post.slug))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_auth_blogindex(self):
        self.assertTrue(self.client.login(username=self.username,
            password=self.password))
        response = self.client.get('/blog/')
        found_unpubbed_post = False
        for post in response.context['posts']:
            if post.name == 'Test post #4':
                found_unpubbed_post = True
        response = self.client.get('/blog/?page=2')
        for post in response.context['posts']:
            if post.name == 'Test post #4':
                found_unpubbed_post = True
        self.assertTrue(found_unpubbed_post)
        self.client.logout()
