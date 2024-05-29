from django.contrib import admin

from . import models
# Register your models here.

class OpinionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "fecha_actualizacion",
    )
    list_display_links = ("titulo", )

admin.site.register(models.Opinion)