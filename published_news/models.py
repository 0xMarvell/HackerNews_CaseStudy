from django.db import models

# Create your models here.
class PublishedNews(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField()
    by = models.CharField(max_length=200)
    score = models.IntegerField()
    item_type = models.CharField(max_length=50)
    descendants = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title