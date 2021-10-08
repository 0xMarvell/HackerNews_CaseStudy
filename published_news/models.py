from django.db import models

# Create your models here.
class PublishedNews(models.Model):
    title = models.CharField()
    url = models.URLField()
    by = models.CharField()
    score = models.IntegerField()
    item_type = models.CharField()
    descendants = models.IntegerField()

