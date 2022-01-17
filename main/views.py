from django.shortcuts import render
from .models import ToDoList

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def allLists(request):
    listObjects = ToDoList.objects
    return render(request, "allLists.html", {"listObjects": listObjects})