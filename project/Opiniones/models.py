from django.db import models

class Opinion(models.Model):
    titulo = models.CharField(max_length=200)
    reseña = models.CharField(max_length=100000000)

    def __str__(self):
        return self.titulo 

