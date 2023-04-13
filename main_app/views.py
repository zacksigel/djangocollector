from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def djangos_detail(request, django_id):
  django = Film.objects.get(id=django_id)
  return render(request, "djangos/detail.html", {"django": django})

class DjangosCreate(CreateView):
  model = Film
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class DjangosUpdate(UpdateView):
  model = Film
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"

class DjangosDelete(DeleteView):
  model = Film
  success_url = "/djangos/"
  template_name = "djangos/django_confirm_delete.html"