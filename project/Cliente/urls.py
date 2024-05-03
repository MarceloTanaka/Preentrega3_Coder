from django.urls import path
from . import views

app_name = "Cliente"

urlpatterns = [
    path("", views.home, name="home"),
    path("cliente/crearcliente", views.crearclientes, name="crearclientes")
]