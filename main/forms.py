from django.forms import ModelForm
from .models import ToDoList

class CreateTableForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]