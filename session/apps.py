from django.apps import AppConfig


class SessionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'session'
    verbose_name = 'Сессия'
    verbose_name_plural = 'Сессии'