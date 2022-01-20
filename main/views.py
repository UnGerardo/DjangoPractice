from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList
from .forms import CreateTableForm

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def allLists(request):
    listObjects = ToDoList.objects
    return render(request, "allLists.html", {"listObjects": listObjects})

def listById(request, id):
    todolist = ToDoList.objects.get(id=id)
    return render(request, "listById.html", {"todolist": todolist})

def createTable(request):
    if request.method == "POST":
        form = CreateTableForm(request.POST)
        if form.is_valid():
            newTable = ToDoList(name=form.cleaned_data["name"], user=request.user)
            newTable.save()
            return HttpResponseRedirect(f"/list/{newTable.id}")
    else:
        form = CreateTableForm()
    return render(request, "create.html", {"form": form})