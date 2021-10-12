from django.db import models

import django_filters

# Create your models here.
class PublishedNew(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    by = models.CharField(max_length=200)
    score = models.IntegerField()
    item_type = models.CharField(max_length=50)
    comments = models.IntegerField()
    hacker_news_id = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=500)
    by = models.CharField(max_length=200)
    item_type = models.CharField(max_length=50)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.text




class NewsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = PublishedNew
        fields = ['item_type']


class CommentsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Comment
        fields = ['item_type']