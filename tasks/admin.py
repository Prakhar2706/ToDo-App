from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_username')
    def get_username(self, obj):
        return obj.user.username if obj.user else 'No User'
    get_username.short_description = 'Username'

admin.site.register(Task, TaskAdmin)
admin.site.register(Profile)
