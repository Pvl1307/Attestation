# Attestation
Веб-приложение с API интерфейсом и админ-панелью по закупкам и поставщикам
## Технологии

![alt text](https://img.shields.io/badge/python-3.11.6-%233776AB?logo=python)
![alt text](https://img.shields.io/badge/django-5.0-%23092E20?logo=django)
![alt text](https://img.shields.io/badge/DRF-3.14.0-%23092E20?logo=drf)
![alt text](https://img.shields.io/badge/PostgreSQL-v16-%234169E1?logo=PostgreSQL)

## Описание
Веб-приложение с API интерфейсом и админ-панелью

**Админ-панель выводит:**
 - ссылку на «Поставщика»;
 - фильтр по названию города;
 - «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

**Используя DRF, было реализовано:**
 - CRUD для модели поставщика (c запретом обновление через API поля «Задолженность перед поставщиком»);
 - Возможность фильтрации объектов по определенной стране.
 - Настройка прав доступа к API так, чтобы только активные сотрудники имели доступ к API.

## Установка

1. Скачайте проект в домашнюю директорию командой: 
   ```ini
   git clone git@github.com:Pvl1307/Attestation.git
   ```
2. Активируйте виртуальное окружение командой: `poetry shell`
3. Установите зависимости командой: `poetry install`

## Перед первым запуском программы:

1. Создайте Базу данных (в данной работе используется PostgreSQL) и перейдите в файл .env.sample и пропишите переменные
   окружения в формате(все данные после "=" в виде примера):

```ini
SECRET_KEY = 'django-secret-key'
DEBUG = True/False

DATABASE_NAME = 'name_of_db'
DATABASE_USER = 'db_user'
DATABASE_PASSWORD = 'your_password'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 5432
```

2. Выполните команды:
   - Для миграции в базу данных: `python manage.py migrate`
   - Команда для запуска сервера: `python manage.py runserver`

## Для завершения работы

В терминале, где запущен сервер, прожать **Ctrl + C**