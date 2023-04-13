from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.
def home(request):
  return render(request, "about.html")

def about(request):
  return render(request, "about.html")

# Add new view
def djangos_index(request):
  djangos = Film.objects.all()
  return render(request, 'djangos/index.html', {'djangos': djangos})

def djangos_detail(request, django_title):
  django = Film.objects.get(title=django_title)
  return render(request, "djangos/detail.html", {"django": django})