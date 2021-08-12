import datetime
import json

import feedparser
from django.contrib.auth.models import User
from django.test import client
from django.test.testcases import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from ..models import Article
from ..serializers import ArticleSerializer
from .factory import ArticleFactory

#import pdb; pdb.set_trace()

# Test case:
# Check news count when parsing news feed url
# Check if worker is finished and stored articles
class TestRssNewsFeed(TestCase):

    def setUp(self):
        User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.c = client.Client()
        self.c.login(username='superuser', password='secret')

    def tearDown(self):
        self.c.logout()

    def test_rss_news_count(self):
        feeds = feedparser.parse("https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US")
        count_news = len(feeds.entries)
        self.assertNotEqual(count_news, 0, msg="Feed news list is zero")

    def test_rss_news_get_and_post(self):
        args = 'AAPL'
        feeds = feedparser.parse("https://feeds.finance.yahoo.com/rss/2.0/headline?s="+args+"&region=US&lang=en-US")
        news = feeds.entries
        for item in news:

            if Article.objects.filter(title=item.title).count() > 0:
                continue
            
            published_date_tp = datetime.datetime.strptime(item.published, "%a, %d %b %Y %H:%M:%S %z").timestamp()
            item_data = {
                "title": item.title,
                "description": item.summary,
                "link": item.link,
                "published": datetime.datetime.fromtimestamp(published_date_tp)
            }
            serializer = ArticleSerializer(data=item_data)
            
            if serializer.is_valid():
                serializer.save()

        message = "Work is finished!"
        # count created articles
        count_articles = len(Article.objects.all())
        self.assertNotEqual(count_articles, 0, msg="Feed news list is zero")
        self.assertEqual(message, "Work is finished!")
        
