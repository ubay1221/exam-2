from django.db import models
from django.shortcuts import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    author = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('articles:detail', args=[self.pk])