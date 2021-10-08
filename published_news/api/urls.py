from django.urls import path
from .views import save_news_to_DB

urlpatterns = [
    path('news/<int:id>/', save_news_to_DB, name='save')
]