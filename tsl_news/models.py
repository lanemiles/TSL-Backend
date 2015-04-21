from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.


# we want article and author and category

class Section(models.Model):
    name = models.CharField(max_length=100, default="No section yet")

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=25, default="No author yet")

    def __unicode__(self):
        return self.name


class Article(models.Model):
    authors = models.ManyToManyField(Author)
    pub_date = models.DateField('date published', default=timezone.now())
    section = models.ForeignKey(Section, null=True)
    is_featured = models.BooleanField(default=False)
    headline = models.CharField(max_length=100, default="No headline yet")
    article_body = models.TextField(default="No article body yet")
    url = models.CharField(max_length=512, default="No link yet")

    def __unicode__(self):
        return self.headline


class WaitingArticle(models.Model):
    url = models.CharField(max_length=512)

    def __unicode__(self):
        return self.url


class User(models.Model):
    iphone_udid = models.CharField(max_length=256)
    favorite_articles = models.ManyToManyField(Article)

    def __unicode__(self):
        return self.iphone_udid

