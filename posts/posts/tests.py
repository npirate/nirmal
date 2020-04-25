#Any function that has the word test* at the beginning and exists in a tests.py file will be run when we execute the command python manage.py test.

from django.test import TestCase
from django.urls import reverse
from .models import Post #we want to check if this method is working correctly and hence we imported it from models

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test') #creating this content in db using the Post method that we have defined

    def test_text_content (self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest (TestCase):
    def setUp(self):
        Post.objects.create(text='another test') #creating this content in db using the Post method that we have defined

    def test_view_url_exists_at_proper_location (self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name_correct_template_used (self):
        resp = self.client.get(reverse('home'))
        self.assertEqual (resp.status_code, 200)
        self.assertTemplateUsed (resp, 'home.html')

