# Generated by Django 5.0.4 on 2024-05-10 12:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_for_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='Баллы')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('body', models.TextField(verbose_name='Текст задания')),
                ('right_answers', models.CharField(help_text='Через запятую без пробелов, например: "1,2,3,сто твадцать три". Поставьте 0 если автопровека будет выключена', max_length=255, verbose_name='Правильные ответы')),
                ('points', models.TextField(blank=True, null=True, verbose_name='Баллы')),
                ('extend_ans_field', models.BooleanField(verbose_name='Расширенное поле для ввода ответа')),
                ('auto_check', models.BooleanField(verbose_name='Автоматическая проверка')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('short_name', models.CharField(max_length=255, verbose_name='Короткое название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('tasks', models.ManyToManyField(to='tests.task', verbose_name='Задания')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.theme', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Answer_from_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, verbose_name='Ответ')),
                ('checked', models.BooleanField(verbose_name='Проверено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.task', verbose_name='Задание')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответы пользователей',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.theme', verbose_name='Тема'),
        ),
    ]