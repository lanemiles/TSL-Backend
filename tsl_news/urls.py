from django.conf.urls import url

from tsl_news import views

urlpatterns = [
    url(r'^articles/$', views.index),
    url(r'^articles/(?P<userID>[-\w]+)/(?P<articleID>\d+)', views.article),
    url(r'^sections/(?P<sectionName>.+)$', views.section),
    url(r'^addArticle/$', views.add_article_url),
    url(r'^featured/$', views.featured),
    url(r'^users/(?P<userID>[-\w]+)$', views.user_favorite),
    url(r'^addFavorite/(?P<userID>[-\w]+)/(?P<articleID>.+)$', views.add_favorite),
    url(r'^removeFavorite/(?P<userID>[-\w]+)/(?P<articleID>.+)$', views.remove_favorite)
]
