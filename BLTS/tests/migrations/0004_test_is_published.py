# Generated by Django 5.0.4 on 2024-05-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_task_img_alter_test_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
