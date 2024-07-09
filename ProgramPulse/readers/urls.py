from django.urls import path
from readers import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_user, name="login")
]