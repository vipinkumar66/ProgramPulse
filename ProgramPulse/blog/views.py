from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Category, Author


def homepage(request):
    # template = get_template("home.html")
    # context = {"":""}
    # return HttpResponse(template.render(context))
    return render(request, 'home.html', {"context":""})


def view_article(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, id=pk)
        if article:
            return render(request, "blog/view_blog.html", {"article":article})
    else:
        return redirect("home")