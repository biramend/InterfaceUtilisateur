from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.form import RegistrationFormUser
from accounts.models import CustomerUser


def signup(request):
    if request.method == "POST":
        form = RegistrationFormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegistrationFormUser()
    return render(request, "accounts/signup.html", {"form": form})


def home(request):
    return render(request, "accounts/home.html")