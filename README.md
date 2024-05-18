# BLTS - Bolgaro4ka Local Test System

Эта тестовая система разработана для школ. В ней можно создавать тесты, сессии, задания. Также для сессий есть лидерборд.

Язык: **Русский**

Backend разработан на: **Django (Python)**

Поддерживает запуск из контейнера (Docker)

## Установка

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

### Ручками
- Скачайте этот репозиторий
- Установите Python (https://python.org/)
- Откройте его в терминале или Git Bash
- выполните команду: `pip install -r req.txt` - она установит все необходимые зависимости.
- Дальше 2 варианта:
  - Для быстрого старта запустите команду: `python s.py <ваш_ip_адрес> <порт>`. Например: `python s.py 192.168.0.16 80`
  - Долгий вариант:
      - Выполняйте данные ниже команды:
          - `py manage.py makemigrations`
          - `python manage.py makemigrations account`
          - `python manage.py makemigrations main`
          - `python manage.py makemigrations session`
          - `python manage.py makemigrations tests`
          - `python manage.py migrate`
          - `python manage.py runserver <ваш_ip_адрес>:<порт>`. Например `python manage.py runserver 192.168.0.16:80`
- Откройте браузер по: ip-адрес:порт



This test system is designed for schools. In it you can create tests, sessions, assignments. There is also a leaderboard for sessions.
Language: **Russian**
