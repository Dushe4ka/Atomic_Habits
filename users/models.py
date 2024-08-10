from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    phone_number = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        blank=True,
        null=True,
        help_text="Укажите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatar/",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    tg_id = models.CharField(
        max_length=50,
        verbose_name="Tg_id",
        blank=True,
        null=True,
        help_text="Укажите tg_id",
    )
    country = models.CharField(
        max_length=100,
        help_text="Укажите страну",
        verbose_name="Страна",
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=100,
        help_text="Укажите город",
        verbose_name="Город",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
