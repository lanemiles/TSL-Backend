# relevant imports
from tsl_news.models import Section, Author, Article, WaitingArticle
import requests
import re
import sys
import lxml
import requests
from lxml import html
import datetime
import json


# make sure HTML scraping works
def test_html_scraping():
    # this should get the HTML from a static TSL article page
    req = requests.get("http://tsl.pomona.edu/articles/2015/4/24/news/6409-city-of-claremont-and-5c-students-join-forces-for-energy-prize")
    # check the request headers
    if not req.status_code == 200:
        print "HTML scraping request did fail"
    if not req.headers['content-type'] == 'text/html; charset=utf-8':
        print "HTML scraping did not return HTML"
    # check for headline
    html = lxml.html.fromstring(req.text)
    if "City of Claremont and 5C Students Join Forces for Energy Prize" not in html.text_content():
        print "Headline not found in HTML scrape"


# make sure all articles have properties
def test_article_has_properties():

    # get each article
    for article in Article.objects.all():
        # get the article
        article = Article.objects.get(id=article.id)
        # get headline
        headline = article.headline
        # make sure it isn't empty
        if headline == '':
            print "(%d) %s does not have a valid title" % (article.id, article.headline[:15])
        # get the authors
        authors = list(article.authors.all())
        if len(authors) == 0:
            print "(%d) %s does not have a valid author" % (article.id, article.headline[:15])
        # get the section
        section = article.section.name
        section_list = []
        for sect in Section.objects.all():
            section_temp = Section.objects.get(id=sect.id)
            section_list.append(section_temp.name)
        if section not in section_list:
            print "(%d) %s does not have a valid section" % (article.id, article.headline[:15])
        # get the date
        date = article.pub_date.strftime("%B %d, %Y")
        if date == '':
            print "(%d) %s is missing a date" % (article.id, article.headline[:15])
        # check body for proper spacing
        article_body = article.article_body
        if "\r" in article_body:
            print "(%d) %s has a carraige return" % (article.id, article.headline[:15])
        if "\n\n\n" in article_body:
            print "(%d) %s has a triple space" % (article.id, article.headline[:15])
        if " \n " in article_body:
            print "(%d) %s has a single space" % (article.id, article.headline[:15])

