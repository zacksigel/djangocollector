from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about/", views.about, name="about"),
  path("djangos/", views.djangos_index, name="index")
]