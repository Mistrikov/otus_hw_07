from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    # Путь для сохранения персональных файлов MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)


class ScUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.TextField(unique=False, null=True, default='')
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name="Фотография")

    def get_lastname(self):
        return self.last_name

    def get_mediapath(self):
        return self.id
