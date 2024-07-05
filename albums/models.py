from django.db import models
from django.utils import timezone
from users.models import User


# Definición del modelo de albumes
class Album(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    visibility = models.BooleanField(default=False, null=False)
    creation_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
