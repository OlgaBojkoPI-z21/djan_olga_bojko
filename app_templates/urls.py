from django.urls import path
from .views import (
    HomePageView, AboutPageView, TextPageView, ResumePageView,
    WeatherCreateView, WeatherUpdateView, WeatherDeleteView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("text/", TextPageView.as_view(), name="text"),
    path("resume/", ResumePageView.as_view(), name="resume"),

    path("weather/new/", WeatherCreateView.as_view(), name="weather_new"),
    path("weather/<int:pk>/edit/", WeatherUpdateView.as_view(), name="weather_edit"),
    path("weather/<int:pk>/delete/", WeatherDeleteView.as_view(), name="weather_delete"),
]
