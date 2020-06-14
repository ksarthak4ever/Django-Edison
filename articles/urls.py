# Django imports.
from django.urls import path

# App imports.
from articles.views import (
	ArticlesListView, MagazinesListView,
	UserArticlesView, MagazineArticlesView,
	ArticleView
)


urlpatterns = [
    # Route to fetch all articles.
    path(r'articles/', ArticlesListView.as_view(), name='article-list'),

    # Route to fetch all magazines.
    path(r'magazines/', MagazinesListView.as_view(), name='magazine-list'),

    # Route to fetch all the articles of a Author/User.
    path(r'authors/<int:user_id>/articles/', UserArticlesView.as_view(), name='author-articles'),

    # Route to fetch all the articles related to the Magazine.
    path(r'magazines/<int:magazine_id>/articles/', MagazineArticlesView.as_view(), name='magazine-articles'),

    # Route to retrieve, update and delete an Article 
    path(r'articles/<int:article_id>/', ArticleView.as_view(), name='article'),
]