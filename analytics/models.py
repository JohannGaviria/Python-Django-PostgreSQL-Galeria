from django.db import models
from django.utils import timezone
from images.models import Image
from users.models import User


# Definición del modelo de visualizacion
class Visualization(models.Model):
    datetime = models.DateTimeField(default=timezone.now, null=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self) -> str:
        return f"{self.image} - {self.user}"
    

# Definición del modelo de descarga
class Download(models.Model):
    datetime = models.DateTimeField(default=timezone.now, null=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self) -> str:
        return f"{self.image} - {self.user}"
