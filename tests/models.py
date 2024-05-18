from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Theme(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_name = models.CharField(max_length=255, verbose_name='Короткое название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    body = models.TextField(verbose_name='Текст задания')
    right_answers = models.CharField(max_length=255, verbose_name='Правильные ответы', help_text='Через запятую без пробелов, например: "1,2,3,сто твадцать три".', null=True, blank=True)
    points = models.FloatField(verbose_name='Баллы', null=True, blank=True)
    img = models.ImageField(upload_to='tasks/img/%Y/%m/%d', verbose_name='Картинка', null=True, blank=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    extend_ans_field = models.BooleanField(verbose_name='Расширенное поле для ввода ответа')
    auto_check = models.BooleanField(verbose_name='Автоматическая проверка')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    def __str__(self):
        return self.title
    

class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    tasks = models.ManyToManyField(Task, verbose_name='Задания')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    img = models.ImageField(upload_to='tests/img/%Y/%m/%d', verbose_name='Картинка', null=True, blank=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
    
class Answer_from_user(models.Model):
    #test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    checked = models.BooleanField(verbose_name='Проверено')

    def __str__(self):
        return f'{self.user.username[:10]} - {self.answer[:15]}'
    
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'


class Tests_for_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    ans = models.ManyToManyField(Answer_from_user, verbose_name='Ответы')
    points = models.FloatField(verbose_name='Баллы', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username[:10]} - {self.test.title[:15]} : {self.points}'
    
    class Meta:
        verbose_name = 'Ответ пользователя на тесты'
        verbose_name_plural = 'Ответы пользователя на тесты'
    
