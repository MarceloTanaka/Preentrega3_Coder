from django.db import models
from django.utils import timezone

class Opinion(models.Model):
    titulo = models.CharField(max_length=200)
    reseña = models.TextField(null=True, blank=True, verbose_name="reseña")
    fecha_actualizacion = models.DateField(
        null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )

    def __str__(self):
        return self.titulo 

