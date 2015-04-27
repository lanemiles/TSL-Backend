# relevant imports
from django.conf.urls import url
from tsl_news import views


# pattern matching the URLs
urlpatterns = [
    url(r'^articles/(?P<userID>[-\w]+)/(?P<articleID>\d+)', views.article, name='indiv_article_view_plus_favorite'),
    url(r'^sections/(?P<sectionName>.+)$', views.section, name='section_list'),
    url(r'^addArticle/$', views.add_article_url, name='add_article_form'),
    url(r'^featured/$', views.featured, name='featured_list'),
    url(r'^users/(?P<userID>[-\w]+)$', views.user_favorite, name='user_favorite_list'),
    url(r'^addFavorite/(?P<userID>[-\w]+)/(?P<articleID>.+)$', views.add_favorite, name='user_add_favorite'),
    url(r'^removeFavorite/(?P<userID>[-\w]+)/(?P<articleID>.+)$', views.remove_favorite, name='user_remove_favorite')
]
