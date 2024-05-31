from django.urls import path
from . import views

app_name = "Cliente"

urlpatterns = [
    path("", views.home, name="home"),
    path("cliente/crearcliente", views.cliente_create, name="cliente_create"),
    path("cliente/cliente_delete/ <int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),
    path("cliente/cliente_detail/ <int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    path("cliente/cliente_update/ <int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
]