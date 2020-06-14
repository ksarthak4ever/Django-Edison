# DRF imports.
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# App imports.
from accounts.models import User
from articles.models import Article, Magazine
from articles.serializers import ArticleSerializer, MagazineSerializer


class ArticlesListView(APIView):
	"""
	API to fetch all the articles.
	"""
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		articles_qs = Article.objects.all()
		article_serializer = ArticleSerializer(articles_qs, many=True)
		return Response(data=article_serializer.data, status=status.HTTP_200_OK)


class MagazinesListView(APIView):
	"""
	API to fetch all the magazines.
	"""
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		magazines_qs = Magazine.objects.all()
		magazine_serializer = MagazineSerializer(magazines_qs, many=True)
		return Response(data=magazine_serializer.data, status=status.HTTP_200_OK)


class UserArticlesView(APIView):
	"""
	API to fetch all the articles of a Author/User.
	"""
	permission_classes = (IsAuthenticated, )

	def get(self, request, user_id=None):
		articles_qs = Article.objects.filter(author=user_id)
		article_serializer = ArticleSerializer(articles_qs, many=True)
		return Response(data=article_serializer.data, status=status.HTTP_200_OK)


class MagazineArticlesView(APIView):
	"""
	API to fetch all the articles related to the Magazine.
	"""
	permission_classes = (IsAuthenticated, )

	def get(self, request, magazine_id=None):
		articles_qs = Article.objects.filter(magazine=magazine_id)
		magazine_serializer = ArticleSerializer(articles_qs, many=True)
		return Response(data=magazine_serializer.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
	"""
	API to retrieve, update and delete an Article.
	"""
	permission_classes = (IsAuthenticated, )

	def get(self, request, article_id=None):

		try:
			article_obj = Article.objects.get(pk=article_id)
		except Exception as e:
			return Response(data=["Invalid Article ID"], status=status.HTTP_400_BAD_REQUEST)

		article_serializer = ArticleSerializer(article_obj)
		return Response(data=article_serializer.data, status=status.HTTP_200_OK)

	def put(self, request, article_id=None):

		req_data = request.data
		try:
			article_obj = Article.objects.get(pk=article_id)
		except Exception as e:
			return Response(data=["Invalid Article ID"], status=status.HTTP_400_BAD_REQUEST)

		article_serializer = ArticleSerializer(article_obj, data=req_data)
		if article_serializer.is_valid():
			article_serializer.save()
			return Response(data=article_serializer.data, status=status.HTTP_200_OK)
		return Response(data=["Invalid data"], status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, article_id=None):

		try:
			article_obj = Article.objects.get(pk=article_id)
		except Exception as e:
			return Response(data=["Invalid Article ID"], status=status.HTTP_400_BAD_REQUEST)

		article_obj.delete()
		return Response(data=["Article Deleted"], status=status.HTTP_204_NO_CONTENT)