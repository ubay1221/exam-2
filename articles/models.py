from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    author = models.CharField(max_length=100)