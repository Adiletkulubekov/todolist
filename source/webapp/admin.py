from django.contrib import admin
from webapp.models import Article

# Register your models here.
admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['describe', 'status', 'schedule_at']
    list_filter = ['status']
    search_fields = ['describe']
