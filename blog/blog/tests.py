from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTest (TestCase):

    def setUp(self):
