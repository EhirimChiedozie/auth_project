from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import User

class CustomUser(AbstractUser, PermissionsMixin):
    bio = models.CharField(max_length=255, blank=True)
    cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)

class Todo(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline_day = models.DateField(max_length=255)