from django.urls import path

from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)
from hexlet_django_blog.article.views import ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='article_index'),
    path(
        '<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'
    ),
    path(
        '<int:id>/delete/',
        ArticleFormDeleteView.as_view(),
        name='articles_delete',
    ),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
