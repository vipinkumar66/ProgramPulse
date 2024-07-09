from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from readers.forms import RegisterationForm, LoginForm

def register(request, *args, **kwargs):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterationForm()
    return render(request, "auth/register.html", {"form":form})

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user_exists = authenticate(request, email=email, password=password)
            if user_exists:
                login(request, user_exists)
                return redirect("home")
            form.add_error(None, "Email or password is incorrect!!")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form":form})