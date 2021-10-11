from django.urls import path

from .views import comment, index

urlpatterns = [
    path('', index, name='index'),
    path('comments/<int:hacker_news_id>/<int:parent_id>/', comment, name='comment')
]
