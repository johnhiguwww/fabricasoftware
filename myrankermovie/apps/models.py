from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie1(models.Model):
    movie1 = models.CharField(max_length=200)

    synopsis1 = models.TextField()

    def __str__(self):
        return f"1º Movie: {self.movie1}, 1º Synopsis: {self.synopsis1}"

class Movie2(models.Model):
    movie2 = models.CharField(max_length=200)

    synopsis2 = models.TextField()

    def __str__(self):
        return f"2º Movie: {self.movie2}, 2º Synopsis: {self.synopsis2}"

class Movie3(models.Model):
    movie3 = models.CharField(max_length=200)

    synopsis3 = models.TextField()

    def __str__(self):
        return f"3º Movie: {self.movie3}, 3º Synopsis: {self.synopsis3}"