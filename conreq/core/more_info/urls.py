from django.urls import path

from . import views

app_name = "more_info"
urlpatterns = [
    path("", views.more_info, name="main"),
    path("person/", views.person, name="person"),
    path("recommended/", views.recommended, name="recommended"),
    path("collection/", views.collection, name="collection"),
    path("series_modal/", views.series_modal, name="series_modal"),
    path(
        "content_preview_modal/",
        views.content_preview_modal,
        name="content_preview_modal",
    ),
]
