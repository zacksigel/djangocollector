from django.db import models

# Create your models here.

class Film(models.Model):
  title = models.CharField(max_length=100)
  director = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  release_date = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title

djangos = [
  Film('Django', 'Sergio Corbucci', 'Spaghetti Western', 1966),
  Film('Django Unchained', 'Quentin Tarantino', 'Western', 2012),
  Film('Sukiyaki Western Django', 'Takashi Miike', 'Japanese Western', 2008)
]