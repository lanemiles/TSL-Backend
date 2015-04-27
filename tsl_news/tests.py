# relevant imports
from tsl_news.models import Section, Author, Article, WaitingArticle
import requests
import lxml
from lxml import html
from django.test import Client
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import setup_test_environment

setup_test_environment()


class ArticleTests(TestCase):

    # should return not favorited
    def test_not_favorite_always(self):
        client = Client()
        req = client.get(reverse('indiv_article_view_plus_favorite', kwargs={'userID' : 'test', 'articleID' : 1}))
        self.assertContains(req, '"favorited" : "false"', status_code = 200)
