from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import PublishedNew, Comment

# Create your views here.
def index(request):
    published_news = PublishedNew.objects.all().order_by('-id')
    p = Paginator(published_news, 10)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)  # returns the desired page object
    page_range = p.page_range # this page range


    return render(
        request, 
        'index.html', 
            {
                'published_news':published_news, 
                'page_obj': page_obj,
                'page_range': page_range
            }
        )

# def news_detail(request, id):
#     comments = PublishedNews.objects.get(id = id)
#     return render (
#         request,
#         'me.html',
#         {'comments': comments}
#     )

def comment(request, hacker_news_id, parent_id):
    p_id = PublishedNew.objects.filter(hacker_news_id=hacker_news_id)
    c_id = Comment.objects.filter(parent_id=parent_id)
    if c_id == p_id:
        comments = Comment.objects.order_by('-id')
        return render(request, 'descendants.html', {'comments':comments})
    else:
        return HttpResponse('This post does not have any comments yet...')