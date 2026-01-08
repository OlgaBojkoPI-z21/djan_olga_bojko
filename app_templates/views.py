from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class TextPageView(TemplateView):
    template_name = "text.html"

class ResumePageView(TemplateView):
    template_name = "resume.html"

class WeatherCreateView(CreateView):
    model = Post
    template_name = "weather_new.html"
    fields = ["date", "temperature", "pressure", "wind_speed", "precipitation"]
    success_url = reverse_lazy("home")

class WeatherUpdateView(UpdateView):
    model = Post
    template_name = "weather_edit.html"
    fields = ["date", "temperature", "pressure", "wind_speed", "precipitation"]
    success_url = reverse_lazy("home")

class WeatherDeleteView(DeleteView):
    model = Post
    template_name = "weather_delete.html"
    success_url = reverse_lazy("home")
