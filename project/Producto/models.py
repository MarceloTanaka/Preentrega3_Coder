from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="imagen", null=True, blank=True)

    def __str__(self):
        return self.nombre