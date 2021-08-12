from .factory import ArticleFactory
from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import datetime

# Test client as super user

def get_admin_change_view_url(obj: object) -> str:
    return reverse(
        'admin:{}_{}_change'.format(
            obj._meta.app_label,
            type(obj).__name__.lower()
        ),
        args=(obj.pk,)
    )


class TestGroupAdmin(TestCase):

    def setUp(self):
        # prepare client
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.c = Client()
        self.c.login(username='superuser', password='secret')  

    def tearDown(self):
        self.c.logout()

    # Check admin tests
    def test_change_view_loads_normally(self):

        # create test data
        my_group = Group.objects.create(name='Test Group')

        # run test
        response = self.c.get(get_admin_change_view_url(my_group))
        self.assertEqual(response.status_code, 200)

class TestArticleAdmin(TestCase):

    def setUp(self):
        # prepare client and create articles
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.c = Client()
        self.c.login(username='superuser', password='secret')  
        
        self.article_list = ArticleFactory.build_batch(10)


    def tearDown(self):
        self.c.logout()

    # Find any article
    def test_list_article(self):
        article = self.article_list[0]
        response = self.c.get(get_admin_change_view_url(article))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    
    # Find first article
    def test_find_article(self):
        article = self.article_list[0]
        response = self.c.get(get_admin_change_view_url(article))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
