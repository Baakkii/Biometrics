import profile

from django.urls import path

from . import views, profile_view

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", profile_view.profile, name="profile"),
]