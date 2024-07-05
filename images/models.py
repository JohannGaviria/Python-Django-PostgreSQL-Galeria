from django.db import models
from django.utils import timezone
from users.models import User
from albums.models import Album


# Definición del modelo de imagen
class Image(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/', null=False)
    upload_date = models.DateTimeField(default=timezone.now, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.image
