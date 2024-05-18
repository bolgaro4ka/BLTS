from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте дополнительные поля, которые вы хотите включить в профиль пользователя
    user_class = models.CharField(max_length=4, verbose_name='Класс', null=True, blank=True)

    # Опционально: метод для получения дополнительной информации о пользователе

# Для создания объекта UserProfile после создания пользователя, используйте сигналы
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
'''