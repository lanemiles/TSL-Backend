# relevant imports
from django.conf.urls import include, url
from django.contrib import admin

# pattern matching the URLs
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tsl_news.urls')),
]
