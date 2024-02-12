from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'timestamp',
    )  # Перечисляем поля, отображаемые в таблице списка статей
    list_filter = (
        ('timestamp', DateFieldListFilter),
    )  # Перечисляем поля для фильтрации
    search_fields = ['name', 'body']


# admin.site.register(Article)
