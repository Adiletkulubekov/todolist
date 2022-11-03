from django.contrib import admin
from webapp.models import Todolist

# Register your models here.
admin.site.register(Todolist)


class TodolistAdmin(admin.ModelAdmin):
    list_display = ['describe', 'status', 'schedule_at']
    list_filter = ['status']
    search_fields = ['describe']
