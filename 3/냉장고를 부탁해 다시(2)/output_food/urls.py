from django.urls import path
from . import views


app_name = "output"

urlpatterns = [
    path("", views.index, name="index"),
    path("/registration", views.registration, name="registration"),
]
