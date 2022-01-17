from django.urls import path
from .views import index, allLists, listById

urlpatterns = [
    path("", index, name="Index"),
    path("all/", allLists, name="All Lists"),
    path("list/<int:id>", listById, name="List By Id"),
]