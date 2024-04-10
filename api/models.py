from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=255)

    posts = models.ManyToManyField("Post")


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

