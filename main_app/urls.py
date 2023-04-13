from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("about/", views.about, name="about"),
  path("djangos/", views.djangos_index, name="index"),
  path("djangos/<int:django_id>/", views.djangos_detail, name="detail"),
  path("djangos/create/", views.DjangosCreate.as_view(), name="djangos_create"),
  path("djangos/<int:pk>/update/", views.DjangosUpdate.as_view(), name="djangos_update"),
  path("djangos/<int:pk>/delete/", views.DjangosDelete.as_view(), name="djangos_delete"),
]