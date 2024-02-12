from django.views import View
from django.shortcuts import render, get_object_or_404

from hexlet_django_blog.article.models import Article


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
            },
        )


class ArticleView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        return render(
            request,
            'articles/show.html',
            context={
                'article': article,
            },
        )
