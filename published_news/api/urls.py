from django.urls import path

from .views import PublishedNews, UpdateNews, Comments

urlpatterns = [
    # Allows filtering by item type, by, score, comments - ?add item_type='item type'
    path('', PublishedNews.as_view(), name='api-index'), 
    path('<int:pk>/update/', UpdateNews.as_view(), name='api-update'),
    path('<int:pk>/delete/', UpdateNews.as_view(), name='api-delete'),

    path('comments', Comments.as_view(), name='api-comments'),
]
