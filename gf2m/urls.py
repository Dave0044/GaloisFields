from django.urls import path
from . import views

app_name = "gf2m"
urlpatterns = [
    path("", views.start, name="start"),  # Esta es la ruta para la URL raíz
    path("index/", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("addition/", views.addition, name="addition"),
    path("multiplication/", views.multiplication, name="multiplication"),
    path("division/", views.division, name="division"),
    path("polyoperations/", views.polyoperations, name="polyoperations"),
]
