from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Django, Home_Video_Release
from .forms import ScreeningForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, "about.html")

def about(request):
  return render(request, "about.html")

@login_required
def djangos_index(request):
  djangos = Django.objects.filter(user=request.user)
  return render(request, 'djangos/index.html', {
    'djangos': djangos,
    })

@login_required
def djangos_detail(request, django_id):
  django = Django.objects.get(id=django_id)
  not_released_on = Home_Video_Release.objects.exclude(id__in = django.home_video_releases.all().values_list("id"))
  screening_form = ScreeningForm()
  return render(request, "djangos/detail.html", {
    'django': django,
    "screening_form": screening_form,
    "not_released_on": not_released_on
    })

@login_required
def add_screening(request, django_id):
  form = ScreeningForm(request.POST)
  if form.is_valid():
    new_screening = form.save(commit=False)
    new_screening.django_id = django_id
    new_screening.save()
  return redirect("detail", django_id=django_id)

@login_required
def assoc_home_video_release(request, django_id, home_video_release_id):
  django = Django.objects.get(id=django_id)
  django.home_video_releases.add(home_video_release_id)
  return redirect("detail", django_id=django_id)

@login_required
def unassoc_home_video_release(request, django_id, home_video_release_id):
  django = Django.objects.get(id=django_id)
  django.home_video_releases.remove(home_video_release_id)
  return redirect("detail", django_id=django_id)

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("djangos_index")
        else:
            error_message ="Invalid signup, try again"
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form,
                                                         "error": error_message})

class DjangosCreate(LoginRequiredMixin, CreateView):
  model = Django
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class DjangosUpdate(LoginRequiredMixin, UpdateView):
  model = Django
  fields = ("title", "director", "genre", "release_date")
  template_name = "djangos/django_form.html"

class DjangosDelete(LoginRequiredMixin, DeleteView):
  model = Django
  success_url = "/djangos/"
  template_name = "djangos/django_confirm_delete.html"
