from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Django
from .forms import ScreeningForm

# Create your views here.
def home(request):
  return render(request, "about.html")

def about(request):
  return render(request, "about.html")

# Add new view
def djangos_index(request):
  djangos = Django.objects.all()
  return render(request, 'djangos/index.html', {
    'djangos': djangos,
    })

def djangos_detail(request, django_id):
  django = Django.objects.get(id=django_id)
  screening_form = ScreeningForm()
  return render(request, "djangos/detail.html", {
    'django': django,
    "screening_form": screening_form
    })

def add_screening(request, django_id):
  form = ScreeningForm(request.POST)
  if form.is_valid():
    new_screening = form.save(commit=False)
    new_screening.django_id = django_id
    new_screening.save()
  return redirect("detail", django_id=django_id)

class DjangosCreate(CreateView):
  model = Django
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"
  # def form_valid(self, form):
  #   form.instance.user = self.request.user
  #   return super().form_valid(form)
  
class DjangosUpdate(UpdateView):
  model = Django
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"

class DjangosDelete(DeleteView):
  model = Django
  success_url = "/djangos/"
  template_name = "djangos/django_confirm_delete.html"
