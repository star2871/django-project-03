from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.TextField()
    grade = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
