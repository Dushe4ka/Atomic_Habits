from datetime import datetime, date, timedelta
from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


def create_meassage(habit):
    """Функция для создания сообщения"""
    if habit.reward:
        text_reward = f"После этого я могу {habit.reward}"
    else:
        text_reward = f"После этого я могу {habit.related_habit.action}"
        message = (
            f"Напоминание! Сегодня в {habit.time} в {habit.place} я буду {habit.action}"
            f" в течении {habit.period_time}. {text_reward}. Все получится!"
        )
    return message


@shared_task
def send_habit_reminder():
    """Функция проверяет все привычки. Отправляет напоминание о выполнение
        привычки в опреленное время и дату.
        После этого дата выполнения привычки меняется"""
    habits_list = Habit.objects.filter(is_pleasant=False)
    print(habits_list)
    for habit in habits_list:
        current_date = date.today()
        current_time = datetime.now().time().replace(second=0, microsecond=0)
        chat_id = habit.owner.tg_id
        message = create_meassage(habit)
        if habit.habit_date == current_date or not habit.habit_date:
            if habit.time >= current_time:
                send_telegram_message(chat_id, message)
                print("Сообщение отправляется")
                habit.habit_date = current_date + timedelta(days=habit.periodicity)
                habit.save()

