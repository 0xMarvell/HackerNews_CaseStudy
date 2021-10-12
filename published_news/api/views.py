from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from published_news.models import PublishedNew, Comment
from .serializers import PublishedNewsSerializer, CommentSerializer


class PublishedNews(generics.ListCreateAPIView):
    queryset = PublishedNew.objects.all().order_by('-id')
    serializer_class = PublishedNewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item_type','by','comments','score']


class UpdateNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = PublishedNew.objects.all().order_by('-id')
    serializer_class = PublishedNewsSerializer


class Comments(generics.ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','by','parent_id']

