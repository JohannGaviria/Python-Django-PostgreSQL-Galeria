from django.db import models
from django.utils import timezone
from images.models import Image
from users.models import User


# Definición del modelo de comentario
class Comment(models.Model):
    comment = models.TextField(null=False)
    comment_date = models.DateTimeField(default=timezone.now, null=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.comment
