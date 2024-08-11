Веб-приложения "Трекер полезных привычек".
Автор: Голубинец П.Ю.

Технологии:
python 3.12, postgresql, Redis, API

Используемые библиотеки:
Django, djangorestframework, djangorestframework-simplejwt, celery, django-celery-beat,
pillow, psycopg2-binary, python-dotenv, redis, django-cors-headers, drf-yasg

Инструкция для развертывания проекта:
1. Клонировать проект: https://github.com/Dushe4ka/Atomic_Habits
2. Создать виртуальное окружение. Для этого в терминале запустить команды:
python -m venv source venv/bin/activate
3. Установить зависимости. Для установки всех зависимостей в терминале запустить команду:
pip install -r requirements.txt
4. Cоздать базу данных. Для этого в терминале введите команду:
CREATE DATABASE database_name
5. Создать и применить миграции. Для этого в терминале введите команды:
python3 manage.py makemigrations
python3 manage.py migrate
6. Заполнить файл .env по образцу .env.sample
7. Cоздать суперпользователя. Для этого необходимо применить команду:
python3 manage.py csu
8. Запустить проект через следующую команду:
python manage.py runserver
9.1 Для работы с приложением необходима регистрация, нужно ввести обязательные поля:
password, email, tg_id (ваш id в telegram)
После регистрации вы сможете добавить свои привычки, вознаграждения и активировать рассылку-напоминание.
9.2 Для подключения бота в Телеграм перейти по ссылке: t.me/yuliana_habit_bot
10. Для запуска периодических задач необходимо применить команду:
celery -A config worker --beat --scheduler django --loglevel=info
либо
для запуска Celery worker в первом терминале: celery -A config worker -l INFO -P eventlet
для запуска планировщика Celery beat в другом терминале: celery -A config beat -l INFO
Celery worker и Celery beat будут совместно работать для выполнения периодических задач.
11. Документация API:
Swagger http://127.0.0.1:8000/docs/
Redoc http://127.0.0.1:8000/redoc/

Задача проекта.

Добавьте необходимые модели привычек. Реализуйте эндпоинты для работы с фронтендом.
Создайте приложение для работы с Telegram и рассылками напоминаний.

Модели
Хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:
я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку.
Но при этом привычка не должна расходовать на выполнение больше двух минут.
Исходя из этого получаем первую модель — «Привычка».

Привычка:
Пользователь — создатель привычки. Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку. Действие — действие, которое представляет собой привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.

Валидаторы
Исключить одновременный выбор связанной привычки и указания вознаграждения.
В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.
Время выполнения должно быть не больше 120 секунд. В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки. Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели.
За одну неделю необходимо выполнить привычку хотя бы один раз.

Пагинация
Для вывода списка привычек реализовать пагинацию с выводом по 5 привычек на страницу.

Права доступа
Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Эндпоинты
Регистрация. Авторизация. Список привычек текущего пользователя с пагинацией. Список публичных привычек.
Создание привычки. Редактирование привычки. Удаление привычки.
Интеграция Для полноценной работы сервиса необходимо реализовать работу с отложенными задачами для напоминания о том,
в какое время какие привычки необходимо выполнять.

Безопасность
Для проекта необходимо настроить CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

Документация
Для реализации экранов силами фронтенд-разработчиков необходимо настроить вывод документации.
