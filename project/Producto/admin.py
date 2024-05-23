from django.contrib import admin

from . import models
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
        "precio",
        "imagen",
        )

admin.site.register(models.Producto)