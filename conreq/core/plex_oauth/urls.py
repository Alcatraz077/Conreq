from django.urls import path
from . import views

app_name = "plex_oauth"
urlpatterns = [
    path("", views.plex_oauth, name="main"),
]