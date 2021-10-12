from django.urls import path

from .views import filter_comments, filter_news, index, search_results

urlpatterns = [
    path('', index, name='index'),
    # path('<int:post_id>/comments/<int:hacker_news_id>/<int:parent_id>/', comments, name='comment'),
    path('search', search_results, name='search-results'),
    path('filter-news', filter_news, name='filter-results-news'),
    path('filter-comments', filter_comments, name='filter-results-comments'),
]
