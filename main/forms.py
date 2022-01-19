from django import forms

class CreateTableForm(forms.Form):
    name = forms.CharField(label="Table Name:", max_length=200)