from django.db import models
from images.models import Image


# Definición del modelo de etiqueta
class Label(models.Model):
    tag_name = models.CharField(max_length=100, null=False, unique=True)


    def __str__(self):
        return self.tag_name


# Definición del modelo imagen/etiqueta
class ImageTag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False)
    label = models.ForeignKey(Label, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.image} - {self.label}"
