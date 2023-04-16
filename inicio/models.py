from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.URLField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    reproducciones = models.IntegerField(default=0)
    creado_en = models.DateTimeField(auto_now_add=True)