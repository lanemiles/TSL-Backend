from django.test import TestCase

from tsl_news.models import Section, Author, Article, WaitingArticle, User


def article_has_author():
    article_list = Article.objects.all()
