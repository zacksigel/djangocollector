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
  path('djangos/<int:django_id>/add_screening/', views.add_screening, name='add_screening'),
  path("djangos/<int:django_id>/assoc_release/<int:home_video_release_id>/", views.assoc_home_video_release, name="assoc_home_video_release"),
  path("djangos/<int:django_id>/unassoc_release/<int:home_video_release_id>/", views.unassoc_home_video_release, name="unassoc_home_video_release"),
  path('accounts/signup/', views.signup, name='signup')
]