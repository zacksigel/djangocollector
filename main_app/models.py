from django.db import models
from django.urls import reverse


# Create your models here.

class Django(models.Model):
  title = models.CharField(max_length=100)
  director = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  release_date = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse('detail', kwargs={'django_id': self.id})
  
class Screening(models.Model):
  THEATERS = (
     ("P", "Pantheon"),
     ("W", "Worlds Theater"),
     ("R", "Regal Cinemas"),
  )

  date = models.DateField("screening date")
  theater = models.CharField(max_length=1, choices=THEATERS, default=THEATERS[0][0], verbose_name="theater")
  django = models.ForeignKey(Django, on_delete=models.CASCADE)
  def __str__(self):
     return f"Playing at {self.get_theater_display()} on {self.date}"
  
  class Meta:
    ordering = '-date',