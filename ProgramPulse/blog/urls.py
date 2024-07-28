from django.urls import path
from blog.views import homepage, view_article, get_all_blogs

urlpatterns = [
    path('', homepage, name="home"),
    # path("create_article", create_article, name="create_article"),
    path("article/<int:pk>", view_article, name="view_article"),
    path("article/all", get_all_blogs, name="allblogs")
]