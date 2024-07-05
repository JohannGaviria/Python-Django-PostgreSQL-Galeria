from django.db import models
from images.models import Image
from users.models import User


# Definición del modelo de like
class Like(models.Model):
    like = models.BooleanField(null=False)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True)


    def __str__(self):
        return self.like
