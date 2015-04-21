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

# takes in a URL and adds it to the database
def scrape(url):

    # get the HTML
    req = requests.get(url)
    html = lxml.html.fromstring(req.text)

    # get article title
    title = html.xpath('//*[@id="aColumn"]/header/h1')[0].text_content()

    # get the section
    try:
        section = html.xpath('//*[@id="aColumn"]/header/div[2]/div[1]')[0].text_content()
    except:
        section = html.xpath('//*[@id="aColumn"]/header/div/div[1]')[0].text_content()

    # get authors
    author_list = html.xpath('//*[@id="aColumn"]/header/div[2]/a /text()')

    if not author_list:
        author_list = html.xpath('//*[@id="aColumn"]/header/div/a /text()')

    # get date
    try:
        date = html.xpath('//*[@id="aColumn"]/header/div[2]/div[2]')[0].text_content().strip()
    except:
        date = html.xpath('//*[@id="aColumn"]/header/div/div[2]')[0].text_content().strip()

    gooddate = datetime.datetime.strptime(date, '%b %d, %Y').strftime('%Y-%m-%d')

    # get article body
    article = html.xpath('//*[@id="aColumn"]//p')
    article.pop()

    # remove line breaks
    for idx, val in enumerate(article):
        if not val.text_content().isspace():
            article[idx] = val.text_content().replace('\r', '').replace('\n', ' ')
        else:
            article[idx] = ''

    # remove paragraphs that are blank
    article = [x for x in article if x != '']

    # condense to string
    article = '\n\n'.join(article)

    # now add this to Django
    new_article, need_to_create = Article.objects.get_or_create(headline=title)
    new_article.headline = title
    new_article.pub_date = gooddate
    get_section, need_to_create = Section.objects.get_or_create(name=section)
    new_article.section = get_section

    new_article.save()

    for one_author in author_list:
        get_author, need_to_create = Author.objects.get_or_create(name=one_author)
        new_article.authors.add(get_author)

    new_article.article_body = article
    new_article.url = url

    new_article.save()

# get all links waiting to be added
lst = []
article_list = WaitingArticle.objects.all()
for art in article_list:
    lst.append(art.url)

counter = 0

# add all links to Article database
for url in lst:
    scrape(url)
    counter = counter + 1
    print '%d' % counter

# once added, delete all WaitingArticles
WaitingArticle.objects.all().delete()
