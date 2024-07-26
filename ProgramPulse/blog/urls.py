from django.urls import path
from blog.views import homepage, view_article

urlpatterns = [
    path('', homepage, name="home"),
    # path("create_article", create_article, name="create_article"),
    path("article/<int:pk>", view_article, name="view_article")
]