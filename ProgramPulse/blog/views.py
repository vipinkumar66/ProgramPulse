from django.shortcuts import render

# This will have the homepage

def homepage(request):

    return render(request, 'home.html', {"context":""})
