from rest_framework.serializers import ValidationError


class RelatedHabitOrRewardValidator:
    """Проверка заполнения полей связанной привычки и вознаграждения:
    должно быть заполнено только одно поле"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        if related_habit and reward:
            raise ValidationError(
                "Два поля связанной привычки и вознаграждения не могут быть заполнены вместе, "
                "выберите что-то одно"
            )


class PleasantHabitValidator:
    """Проверка на отсутствие у приятной привычки полей связанной привычки и вознаграждения"""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_pleasant = dict(value).get(self.field3)
        if is_pleasant:
            if reward or related_habit:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения "
                    "или связанной привычки."
                )


class DurationTimeValidator:
    """Проверка продолжительности выполнения привычки: не более 2 минут"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period_time = dict(value).get(self.field)
        if period_time and period_time > 120:
            raise ValidationError(
                "Продолжительность выполнения привычки не может превышать 2 минуты."
            )


class PeriodicityValidator:
    """Проверка периодичности выполнения привычки не реже,
    чем 1 раз в 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if periodicity:
            if not 1 <= periodicity <= 7:
                raise ValidationError(
                    "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
                )


class RelatedHabitValidator:
    """Проверка на принадлежность связанной привычки к приятным:
    связать с полезной привычкой можно только приятную привычку
    """

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_pleasant = dict(value).get(self.field2)
        if related_habit and not is_pleasant:
            raise ValidationError(
                "В связанные привычки могут попадать "
                "только привычки с признаком приятной привычки."
            )