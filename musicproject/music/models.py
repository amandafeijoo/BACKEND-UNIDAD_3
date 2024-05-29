from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    genre = models.CharField(max_length=200, default='unknown') 
    popularity = models.IntegerField(default=0)
    

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    popularity = models.IntegerField(default=0)