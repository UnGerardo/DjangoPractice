from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data["username"],
                email = form.cleaned_data["email"],
                password = form.cleaned_data["password1"]
            )
            user.save()
            return HttpResponseRedirect("/login/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})