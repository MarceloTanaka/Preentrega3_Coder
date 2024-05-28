# Generated by Django 5.0.4 on 2024-05-28 22:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Opiniones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='fecha_actualizacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False, null=True, verbose_name='fecha de actualización'),
        ),
    ]