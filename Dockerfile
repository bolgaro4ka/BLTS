FROM python:3.10

WORKDIR /usr/src/app
COPY req.txt ./
RUN pip install -r req.txt
RUN python manage.py makemigrations
RUN python manage.py makemigrations account
RUN python manage.py makemigrations main
RUN python manage.py makemigrations session
RUN python manage.py makemigrations tests
RUN python manage.py migrate session
RUN python manage.py migrate account
RUN python manage.py migrate main
RUN python manage.py migrate tests
RUN python manage.py migrate
