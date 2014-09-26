from django.test import TestCase

from projects.models import get_slug, Project, ProjectImage

# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        proj1 = Project.objects.create(priority=2, name='test proj 1',
                short_descr='Short description 1',
                full_descr = 'Long description 1')
        proj2 = Project.objects.create(priority=1, name='test proj 2',
                link='http://www.test.com/', short_descr = 'Short descr 2',
                full_descr = 'Long descr 2')
        projimg1 = ProjectImage.objects.create(project=proj1,
                image='/tmp/test.jpg')
        projimg2 = ProjectImage.objects.create(project=proj2,
                image='/tmp/test.png')

    def test_get_slug(self):
        proj = Project.objects.get(name='test proj 1')
        img = proj.projectimage_set.first()
        self.assertEqual(get_slug(img, '/foo/bar/baz.jpg'), 'test-proj-1.jpg')

    def test_proj_priority(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['projects'][0].name, 'test proj 2')

    def test_proj_details(self):
        proj = Project.objects.get(name='test proj 2')
        self.assertEqual(proj.slug, 'test-proj-2')
        response = self.client.get('/projects/' + proj.slug + '/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['project'].name, 'test proj 2')
        self.assertTrue(response.context['html'] is not None)
