from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# Definición del modelo de usuarios
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    register_date = models.DateTimeField(default=timezone.now, null=False)
    photo_profile = models.ImageField(upload_to='uploads/users/', blank=True, null=True)
    public_profile = models.BooleanField(default=True, null=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email
