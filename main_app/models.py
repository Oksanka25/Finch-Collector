from django.db import models
from django.contrib.auth.models import User


class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    habitat = models.TextField(max_length=200)
    note = models.TextField(max_length=500)
    population = models.TextField(max_length=20)
    threat = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Song(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    length = models.IntegerField(default=0)
    audio = models.CharField(max_length=150, default=0)
    finch = models.ForeignKey(
        Finch, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_bird = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
