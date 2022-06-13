from collections import UserDict
from django.db import models
from pkg_resources import resource_filename
from django.contrib.auth.models import User



# Create your models here.
class Videogame(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('rpg', 'Role Playing Game'),
        ('shooter', 'Shooter'),
        ('sports', 'Sports'),
        ('stealth', 'Stealth'),
        ('rts', 'Real-Time Strategy'),
        ('fighting', 'Fighting'),
        ('mmo', 'Massive Multiplayer Online'),
        ('simulation', 'Simulation'),
        ('horror', 'Horror'),
    ]
    vgtitle=models.CharField(max_length=225)
    vgdevloper=models.CharField(max_length=225)
    vgreleasedate=models.DateField()
    vggenre=models.CharField(max_length=25, choices=GENRE_CHOICES, default='action')

    def __str__(self):
        return self.vgtitle
    
    class Meta:
        db_table='videogame'

class Vgreview(models.Model):
    RATING_CHOICES = [
        (5, '5 Stars'),
        (4,'4 Stars'),
        (3,'3 Stars'),
        (2,'2 Stars'),
        (1,'1 Stars'),
    ]
    vgtitle=models.ForeignKey(Videogame, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    reviewdate=models.DateField(auto_now_add=True)
    rating=models.IntegerField(choices=RATING_CHOICES, default=5)
    reviewtext=models.TextField(default='enter review here')

    def __str__(self):
        return self.vgtitle
    
    class Meta:
        db_table='vgreview'
