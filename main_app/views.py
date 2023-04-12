from django.shortcuts import render
from django.http import HttpResponse
from .models import djangos

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, "about.html")

# Add new view
def djangos_index(request):
  return render(request, 'djangos/index.html', {'djangos': djangos})