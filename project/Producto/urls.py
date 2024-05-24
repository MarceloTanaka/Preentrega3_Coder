from django.urls import path
from . import views

app_name = "Producto"

urlpatterns = [
    path("", views.home, name="home"),
    path("agregarproducto/", views.ProductoCreate.as_view(), name="producto_create"),
    path("productodetail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("productoupdate/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    path("productodelete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete")
]