# Django imports.
from django.contrib import admin

# App imports.
from articles.models import Article, Magazine

# Models registration.
admin.site.register(Magazine)
admin.site.register(Article)