from django.urls import path
from . import views

app_name = "Producto"

urlpatterns = [
    path("", views.home, name="home"),
    path("agregarproducto/", views.agregarproducto, name="agregarproducto"),
    path("productodetail/<int:pk>", views.producto_detail, name="producto_detail"),
    path("productoupdate/<int:pk>", views.producto_update, name="producto_update"),
    path("productodelete/<int:pk>", views.producto_delete, name="producto_delete")
]