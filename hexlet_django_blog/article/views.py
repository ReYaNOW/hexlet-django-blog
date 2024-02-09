from django.shortcuts import render
from django.views import View


class IndexView(View):
    
    def get(self, request, tags='', article_id=''):
        return render(
            request,
            'articles/article.html',
            context={'tags': tags, 'article_id': article_id},
        )
