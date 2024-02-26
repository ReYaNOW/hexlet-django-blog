from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles},
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


class ArticleFormCreateView(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно добавлена')
            
            return redirect('article_index')

        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, id):
        article = Article.objects.get(id=id)
        form = ArticleForm(instance=article)
        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': id},
        )

    def post(self, request, id):
        article = Article.objects.get(id=id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_index')

        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id': id},
        )


class ArticleFormDeleteView(View):
    def post(self, request, id):
        article = Article.objects.get(id=id)
        if article:
            article.delete()
            messages.success(request, 'Статья успешно удалена')
        return redirect('article_index')
