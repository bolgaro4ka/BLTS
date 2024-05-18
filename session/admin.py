from django.contrib import admin

from .models import Session
# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    list_display = ('test', 'created_at', )
    list_filter = ('users', 'test', )
    search_fields = ('users', 'test', )
    filter_horizontal = ('users', 'answers', )
admin.site.register(Session, SessionAdmin)