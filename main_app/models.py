from django.db import models
from django.urls import reverse

# Create your models here.

class Film(models.Model):
  title = models.CharField(max_length=100)
  director = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  release_date = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("detail", kwargs={"django.id": self.id})