from django.db import models
from django.contrib.auth.models import User
from tests.models import Test
from tests.models import Answer_from_user, Tests_for_user
# Create your models here.
class Session(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    users = models.ManyToManyField(User, verbose_name='Пользователи', blank=True)
    answers = models.ManyToManyField(Tests_for_user, verbose_name='Ответы', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_active = models.BooleanField(verbose_name='Активна', default=True)

    def __str__(self):
        return f'{self.title[:15]}'
    
    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'