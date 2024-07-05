from django.shortcuts import render, HttpResponse
from django.template.loader import get_template


def homepage(request):
    # template = get_template("home.html")
    # context = {"":""}
    # return HttpResponse(template.render(context))
    return render(request, 'home.html', {"context":""})
