from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", register, name="Register"),
]