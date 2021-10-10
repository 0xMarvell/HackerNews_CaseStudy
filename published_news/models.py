from django.db import models

# Create your models here.
class PublishedNews(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    by = models.CharField(max_length=200)
    score = models.IntegerField()
    item_type = models.CharField(max_length=50)
    comments = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title