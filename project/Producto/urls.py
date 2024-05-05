from django.urls import path
from . import views

app_name = "Producto"

urlpatterns = [
    path("", views.home, name="home"),
    path("agregarproducto/", views.agregarproducto, name="agregarproducto")
]