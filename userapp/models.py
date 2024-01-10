from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(upload_to=f"media/user/{AbstractUser.username}", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")