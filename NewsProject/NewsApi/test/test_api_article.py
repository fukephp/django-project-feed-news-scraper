import json, datetime

from django.contrib.auth.models import User
from django.test import client
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from ..models import Article
from ..serializers import ArticleSerializer
from .factory import ArticleFactory

fake = Faker()

#import pdb; pdb.set_trace()

# Tests cases 
# 
# Article group name is articles-list
# Full path:
#     - /api/article
#     - /api/article/:id
# 
class ArticleViewSetTestCase(APITestCase):

    article_url = reverse('articles-list')

    def setUp(self):
        # prepare client
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.c = APIClient()
        self.c.login(username='superuser', password='secret')

        # Create article
        self.article = ArticleFactory()


    def tearDown(self):
        self.c.logout()

    # Test create article
    def test_article_create(self):
        data = {
            "title": fake.sentence(), 
            "description": fake.text(), 
            "link": fake.sentence(), 
            "published": datetime.datetime.now()
        }
        response = self.c.post(self.article_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Check failed validation
    def test_article_forms_validation(self):
        response = self.c.post(self.article_url, {"title":"", "description":"www", "link":"ccc", "published": datetime.datetime.now()})
        self.assertEqual(str(response.data['title'][0]), 'This field may not be blank.')

    # Check failed request 
    def test_create_article_required_fields(self):
        response = self.c.post(self.article_url, {"title":"", "description":"www", "link":"ccc", "published": datetime.datetime.now()})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Check user can see article list
    def test_authorized_user_go_article_view_list(self):
        response = self.c.get(self.article_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Check user can see single article 
    def test_authorized_user_go_article_view_detail(self):
        response = self.c.get(self.article_url, {'id': self.article.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check guest can see single article
    def test_non_authorized_user_go_article_view_detail(self):
        self.c.logout()
        response = self.c.get(self.article_url, {'id': self.article.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Check guest can see article list
    def test_non_authorized_user_go_article_view_list(self):
        self.c.logout()
        response = self.c.get(self.article_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

