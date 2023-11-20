# Create your models here.
from django.db import models

# Create your models here.
# 

class SongRecomendation(models.Model):
    trackName = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    album = models.CharField(max_length=120)

    def __str__(self):
        return self.trackName
    
    
    

class SongInput(models.Model):
    inputSong = models.CharField(max_length=120)

    def __str__(self):
        return self.inputSong
    
    