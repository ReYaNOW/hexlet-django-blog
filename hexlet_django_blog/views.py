from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return redirect(
            reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        )


def about(request):
    return render(request, 'about.html')
