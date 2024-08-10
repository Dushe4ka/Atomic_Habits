from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки:
    Поле related_habit указывается только для полезной привычки
    Поле is_nice - признак приятной привычки, можно привязать к полезной
    Поле reward указывается только для полезной привычки,
    если нет привязки к приятной
    """

    owner = models.ForeignKey(
        User,
        verbose_name='Владелец привычки',
        on_delete=models.CASCADE,
        **NULLABLE,
        help_text='Укажите владельца привычки',
        related_name="owner"
    )
    place = models.CharField(
        verbose_name='Место привычки',
        max_length=255,
        **NULLABLE,
        help_text='Укажите место привычки',
    )
    time = models.TimeField(
        default='12:00:00',
        verbose_name='Время в формате MM-ЧЧ',
        help_text='Укажите время привычки',
    )
    action = models.CharField(
        verbose_name='Действие привычки',
        max_length=255,
        help_text='Укажите действие привычки',
    )
    is_pleasant = models.BooleanField(
        verbose_name='Приятная привычка',
        default=False,
        help_text='Поставьте галочку, если привычка приятная',
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='связанная приятная привычка',
        help_text='Указывается только для полезной привычки',
    )
    periodicity = models.PositiveIntegerField(
        verbose_name='Периодичность привычки',
        default=7,
        help_text='Укажите периодичность привычки в днях',
    )
    reward = models.CharField(
        verbose_name='Награда за привычку',
        max_length=255,
        **NULLABLE,
        help_text='Указывается только для полезной привычки, если нет привязки к приятной',
    )
    period_time = models.PositiveIntegerField(
        verbose_name='Период времени привычки в секундах',
        default=60,
        help_text='Укажите период времени привычки в секундах',
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name='Признак публичности',
        help_text='Можно публиковать в общий доступ',
    )
    habit_date = models.DateField(
        verbose_name='Укажите дату начала выполнения привычки ГГ-ММ-ДД',
        **NULLABLE
    )

    def __str__(self):
        return f"{self.action} в {self.time} {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("action",)



