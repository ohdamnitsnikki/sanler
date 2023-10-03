from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
