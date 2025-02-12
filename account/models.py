from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = None  # Убираем имя
    last_name = None  # Убираем фамилию
    email = models.EmailField(unique=True)  # Делаем email уникальным

    USERNAME_FIELD = "email"  # Авторизация по email
    REQUIRED_FIELDS = []  # Убираем обязательные поля, оставляя только email

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    def save(self, *args, **kwargs):
        """Генерируем username из email перед сохранением"""
        if not self.username:
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)
