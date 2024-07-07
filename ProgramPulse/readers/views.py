from django.shortcuts import render, redirect
from readers.forms import RegisterationForm

def register(request, *args, **kwargs):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterationForm()
    return render(request, "auth/register.html", {"form":form})