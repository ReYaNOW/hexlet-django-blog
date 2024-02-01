from django.shortcuts import render


def index(request):
    return render(
        request,
        'articles/article.html',
        context={'app_name': 'hexlet_django_blog.article'},
    )
