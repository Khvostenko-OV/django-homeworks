from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    article_list = Article.objects.order_by('-published_at').prefetch_related('scopes')
    context = {'object_list': article_list}
    return render(request, template, context)
