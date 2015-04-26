# relevant imports
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.core.serializers.json import Serializer
from tsl_news.models import Section, Author, Article, WaitingArticle, User
from tsl_news.forms import URLForm
import json


# displays the JSON for an article
def article(request, userID, articleID):
    user, created = User.objects.get_or_create(iphone_udid=userID)
    article = Article.objects.get(id=articleID)
    favorited = False
    for fav in user.favorite_articles.all():
        if fav == article:
            favorited = True
    favorited = json.dumps(favorited)

    author_list = []
    for auth in article.authors.all():
        author_list.append(auth.name)
    pub_date = article.pub_date.strftime("%B %d, %Y")
    section_name = json.dumps(article.section.name)
    fields = {'fields' : {'favorited' : favorited, 'headline' : article.headline, 'authors' : author_list, 'section' : section_name, 'pub_date' : pub_date, 'url' : article.url, 'article_body' : article.article_body }}
    return HttpResponse(json.dumps(fields), content_type='application/json')


# displays the JSON list for a section
def section(request, sectionName):
    section = Section.objects.filter(name=sectionName)[:1]
    article_list = Article.objects.filter(section=section).order_by('-pub_date')

    json_list = []

    for article in article_list:
        author_list = []
        for auth in article.authors.all():
            author_list.append(auth.name)
        pub_date = article.pub_date.strftime("%B %d, %Y")
        section_name = json.dumps(article.section.name)
        fields = {'fields' : {'headline' : article.headline, 'authors' : author_list, 'section' : section_name, 'pub_date' : pub_date, 'id' : article.id }}
        json_list.append(fields)

    return HttpResponse(json.dumps(json_list), content_type='application/json')


# displays the JSON list of featured articles
def featured(request):
    article_list = Article.objects.filter(is_featured=True)

    json_list = []

    for article in article_list:
        author_list = []
        for auth in article.authors.all():
            author_list.append(auth.name)
        pub_date = article.pub_date.strftime("%B %d, %Y")
        section_name = json.dumps(article.section.name)
        fields = {'fields' : {'headline' : article.headline, 'authors' : author_list, 'section' : section_name, 'pub_date' : pub_date, 'id' : article.id }}
        json_list.append(fields)

    return HttpResponse(json.dumps(json_list), content_type='application/json')


# Displays JSON list of user favorites
def user_favorite(request, userID):

    user = User.objects.filter(iphone_udid=userID)[:1]
    user = list(user[:1])
    user = user[0]
    article_list = user.favorite_articles.all()

    json_list = []

    for article in article_list:
        author_list = []
        for auth in article.authors.all():
            author_list.append(auth.name)
        pub_date = article.pub_date.strftime("%B %d, %Y")
        section_name = json.dumps(article.section.name)
        fields = {'fields' : {'headline' : article.headline, 'authors' : author_list, 'section' : section_name, 'pub_date' : pub_date, 'id' : article.id }}
        json_list.append(fields)

    return HttpResponse(json.dumps(json_list), content_type='application/json')


# Adds a favorite for a user
def add_favorite(request, userID, articleID):
    user, created = User.objects.get_or_create(iphone_udid=userID)

    art = Article.objects.filter(id=articleID)[:1]
    art = list(art[:1])
    art = art[0]
    user.favorite_articles.add(art)
    return HttpResponse("Done")


# Removes a favorite for a user
def remove_favorite(request, userID, articleID):
    user, created = User.objects.get_or_create(iphone_udid=userID)

    art = Article.objects.filter(id=articleID)[:1]
    art = list(art[:1])
    art = art[0]
    user.favorite_articles.remove(art)
    user.save()
    return HttpResponse("Done")


# Adds an article to the database
def add_article_url(request):
    if request.method == 'GET':
        return render(request, 'tsl_news/add_article.html', {})
    else:
        # A POST request: Handle Form Upload
        form = URLForm(request.POST)
        # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['url']
            post = WaitingArticle.objects.create(url=content)
            return HttpResponsePermanentRedirect("/addArticle/")
