from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.db.models import Q

from .models import PublishedNew, Comment, NewsFilter, CommentsFilter

# Create your views here.
def index(request):
    published_news = PublishedNew.objects.all().order_by('-id')
    p = Paginator(published_news, 10)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object


    return render(
        request, 
        'index.html', 
            {
                'published_news':published_news, 
                'page_obj': page_obj
            }
        )


# def comments(request, hacker_news_id, parent_id, post_id):
#     post_id = get_object_or_404(PublishedNew, pk=post_id)
#     p_id = PublishedNew.objects.filter(hacker_news_id=hacker_news_id)
#     c_id = Comment.objects.filter(parent_id=parent_id)
#     if c_id == p_id:
#         comments = Comment.objects.order_by('-id')
#         return render(request, 'comments.html', {'comments':comments})
#     else:
#         return HttpResponse('This post does not have any comments yet...')


def search_results(request):
    query = request.GET.get('q')
    search_results = PublishedNew.objects.filter(
        Q(title__icontains=query) | Q(by__icontains=query)
        ).order_by('-id')

    p = Paginator(search_results, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object
    if search_results:
        return render(
            request, 
            'search_results.html', 
                {
                    'search_results':search_results, 
                    'page_obj': page_obj
                }
            )
    return render(request, 'search_404.html')


def filter_news(request):
    f = NewsFilter(request.GET, queryset=PublishedNew.objects.all().order_by('-id'))

    return render(
        request, 
        'filter_results_news.html', 
            {
                'filter': f
            }
        )


def filter_comments(request):
    f = CommentsFilter(request.GET, queryset=Comment.objects.all().order_by('-id'))

    return render(
        request, 
        'filter_results_comments.html', 
            {
                'filter': f
            }
        )