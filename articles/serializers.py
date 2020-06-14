# Django imports.
from django.contrib.auth import authenticate

# DRF imports.
from rest_framework.serializers import ModelSerializer

# App imports.
from accounts.models import User
from articles.models import Article, Magazine


class AuthorSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email')


class MagazineSerializer(ModelSerializer):
    owner = AuthorSerializer()

    class Meta:
        model = Magazine
        fields = ('id', 'owner', 'name')


class ArticleSerializer(ModelSerializer):
	author = AuthorSerializer()

	class Meta:
		model = Article
		fields = ('id', 'author', 'magazine', 'title', 'content', 'date_posted')
