from django.urls import path
from readers import views


urlpatterns = [
    path("register", views.register, name="register")
]