from django.urls import path
from .views import index, allLists

urlpatterns = [
    path("", index, name="Index"),
    path("all/", allLists, name="All Lists"),
]