from django.db import models
from users.models import CustomUser
import datetime


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Comments(models.Model):
    commenter = models.CharField(max_length=200)
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment