from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Category, Author


def homepage(request):
    # template = get_template("home.html")
    # context = {"":""}
    # return HttpResponse(template.render(context))
    return render(request, 'home.html', {"context":""})


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form instance without committing to the database
            article = form.save(commit=False)

            try:
                vipin_author = Author.objects.get(user__username="vipinlamba")
            except Author.DoesNotExist:
                return redirect('error_page')  # Handle the case where "VIPIN" does not exist

            # Set the author to the "VIPIN" Author instance
            article.author = vipin_author

            # Save the article to the database to generate an ID
            article.save()

            # Handle category assignments
            new_category = form.cleaned_data.get("new_category")
            category = form.cleaned_data.get("category")

            if category:
                article.categories.add(category)
            if new_category:
                new_category_list = new_category.split(",")
                for cate in new_category_list:
                    category, created = Category.objects.get_or_create(name=cate.strip())
                    article.categories.add(category)

            # Save many-to-many relationships
            article.save()
            form.save_m2m()  # Ensure many-to-many fields are saved

            return redirect('home')
    else:
        form = ArticleForm()

    return render(request, 'blog/write_blog.html', {'form': form})

def view_article(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, id=pk)
        # article_id = request.get.GET("articleId")
        # if article_id:
        #     article = Article.objects.filter(id==article_id).first()
        if article:
            return render(request, "blog/view_blog.html", {"article":article})
    else:
        return redirect("home")