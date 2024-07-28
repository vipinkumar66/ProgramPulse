from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Category, Author
from django.contrib.auth.decorators import login_required
from django.utils.text import Truncator
from blog.utils import clean_content, get_first_image

def homepage(request):
    return render(request, 'home.html', {"context":""})

@login_required()
# the login required can be connected to two things:
# => next param and the LOGIN_URL in the settings file
def view_article(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, id=pk)
        if article:
            return render(request, "blog/view_blog.html", {"article":article})
    else:
        return redirect("home")



def get_all_blogs(request):
    if request.method == "GET":
        all_articles = Article.objects.select_related('author__user').all().values("title", "content", "author__user__username", "dateposted")
        truncated_data = [{
            "title": article["title"],
            "author": article["author__user__username"],  # Fetching the author's username
            "posteddate": article["dateposted"],
            "content": clean_content(Truncator(article["content"]).words(50, truncate="...")),
            "img":get_first_image(article["content"])
        } for article in all_articles]
        return render(request, "blog/all_articles.html", {"all_articles": truncated_data})
