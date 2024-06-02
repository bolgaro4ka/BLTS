# BLTS - Bolgaro4ka Local Test System

Эта тестовая система разработана для школ. В ней можно создавать тесты, сессии, задания. Также для сессий есть лидерборд.

Язык: **Русский**

Backend разработан на: **Django (Python)**

Поддерживает запуск из контейнера (Docker)

## Установка и запуск

### С помощью Docker:
- Скачайте этот репозиторий
- Установите Python (https://python.org/)
- Усановите Docker: https://docs.docker.com/get-docker/
- Откройте в терминале или Git Bash папку с проектом.
- Выполните команду: `docker build .`
- Выполните команду: `docker-compose up`
- Откройте браузер по: localhost:80

Проект запустится на 80 порте по внутреннему IP-адресу (0.0.0.0)

**Предпочитайте этот вариант только для тестирования тестовой системы, а не как его полноценное использование**

### Создание нового суперадминистратора (Docker)
Выполните команду: `docker-compose run blts python manage.py createsuperuser`

### Ручками
- Скачайте этот репозиторий
- Установите Python (https://python.org/)
- Откройте его в терминале или Git Bash
- выполните команду: `pip install -r req.txt` - она установит все необходимые зависимости.

## Запуск
- Тут 2 варианта:
  - Для быстрого старта запустите команду: `python s.py <ваш_ip_адрес> <порт>`. Например: `python s.py 192.168.0.16 80`
  - Долгий вариант:
      - Выполняйте данные ниже команды (их необходимо выполнить один раз кроме последней т.к. она запускает сервер):
          - `py manage.py makemigrations`
          - `python manage.py makemigrations account`
          - `python manage.py makemigrations main`
          - `python manage.py makemigrations session`
          - `python manage.py makemigrations tests`
          - `python manage.py migrate`
          - `python manage.py runserver <ваш_ip_адрес>:<порт>`. Например `python manage.py runserver 192.168.0.16:80`
- Откройте браузер по: ip-адрес:порт

### Создание нового суперадминистратора (ручками)
Выполните команду: `python manage.py createsuperuser`

## Создание тестов, сессий и т.д.
Всё находтся в админ-панели! Просто зайдите туда под суперпользователем и редактируйте нужные поля.
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/b346ec3a-fe34-4af8-b3de-1c67539f4b9a)

## Картиночки
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/c14ac17f-59cc-4036-8c7c-eb0c61cb1b5f)
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/742b8c85-dcca-4b2d-9fea-0862e8cfad62)
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/aa2ef3bd-5c38-4c26-af60-a9e249c65d91)
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/09ef5e22-5019-434f-a4b6-e20417fe2a03)


## Introduction (Eng)
This test system is designed for schools. In it you can create tests, sessions, assignments. There is also a leaderboard for sessions.

Language: **Russian**

Backend developed in: **Django (Python)**

Supports running from container (Docker)

## Installation and start

### Using Docker:
- Download this repository
- Install Python (https://python.org/)
- Install Docker: https://docs.docker.com/get-docker/
- Open the project folder in Terminal or Git Bash.
- Run the command: `docker build .`
- Run the command: `docker-compose up`.
- Open a browser at: localhost:80

The project will start on port 80 at the internal IP address (0.0.0.0.0)

**Prefer this option for testing a test system only, not as a full use case**

### Create a new super administrator (Docker)
Run the command: `docker-compose run blts python manage.py createsuperuser`.

### By hand (installation and start)
- Download this repository
- Install Python (https://python.org/)
- Open it in terminal or Git Bash
- Run the command: `pip install -r req.txt` - it will install all necessary dependencies.
- Next, 2 options:
  - For a quick start run the command: `python s.py <your_ip_address> <port>`. For example: `python s.py 192.168.0.16 80`.
  - Long version:
      - Execute the commands given below (they need to be executed once except for the last one because it starts the server):
          - `py manage.py makemigrations`.
          - `python manage.py makemigrations account`
          - `python manage.py makemigrations main`
          - `python manage.py makemigrations session`
          - `python manage.py makemigrations tests`
          - `python manage.py migrate`
          - `python manage.py runserver <your_ip_address>:<port>`. For example `python manage.py runserver 192.168.0.16:80`.
- Open a browser at: ip-address:port

### Create a new super administrator (manually)
Run the command: `python manage.py createsuperuser`.

### Create tests, sessions, etc.
Everything is in the admin panel! Just go there under superuser and edit the required fields.
![image](https://github.com/bolgaro4ka/BLTS/assets/123888141/b346ec3a-fe34-4af8-b3de-1c67539f4b9a)

# Version: 1.0.0-AD
# By Bolgaro4ka (https://github.com/bolgaro4ka)

