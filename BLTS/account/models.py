from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tests.models import Test

# Create your models here.
class UserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    complete_tests = models.ManyToManyField(Test, blank=True, verbose_name="Завершенные тесты")

    @receiver(post_save, sender=User)
    def create_user_userext(sender, instance, created, **kwargs):
        if created:
            UserExt.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_userext(sender, instance, **kwargs):
        instance.userext.save()


    class Meta:
        verbose_name = 'Пользователь (ext)'
        verbose_name_plural = 'Пользователи (ext)'

    def __str__(self) -> str:
        return self.user.username