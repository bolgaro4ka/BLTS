from django.contrib import admin

from .models import Test, Theme, Task, Answer_from_user, Tests_for_user

# Register your models here.


admin.site.site_header = 'BLTS'
admin.site.site_title = 'BLTS'
admin.site.index_title = 'BLTS'



class TestAdmin(admin.ModelAdmin):
    filter_horizontal = ('tasks', )
    list_display = ('title', 'theme', 'description', 'is_published', 'cheating', )
    list_filter = ('theme', )
    search_fields = ('title', 'theme', 'description', 'instructions', )
    list_editable = ('theme', 'is_published', 'cheating', )
admin.site.register(Test, TestAdmin)

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_name', )
    list_filter = ('title', )
    search_fields = ('title', 'short_name', )
admin.site.register(Theme, ThemeAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'theme', )
    list_filter = ('theme', )
    search_fields = ('title', 'theme', )
    

    
admin.site.register(Task, TaskAdmin)

class Tests_for_userAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', )
    list_filter = ('user', 'test', )
    search_fields = ('user', 'test', )
admin.site.register(Tests_for_user, Tests_for_userAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ( 'task', 'user', 'answer', 'checked')   
    list_filter = ( 'task', 'user', 'checked') 
    search_fields = ( 'task', 'user', 'answer')
    list_editable = ('checked', )
admin.site.register(Answer_from_user, AnswerAdmin)


