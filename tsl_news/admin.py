from django.contrib import admin
from tsl_news.models import Section, Author, Article

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Section)
