from django.contrib import admin
from articles.models import ArticleModel
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
        'is_active',
        'created_at'
    ]

    list_editable = ['is_active']
    search_fields = ['title']

    list_filter = [
        'is_active',
        ('created_at',JDateFieldListFilter)
    ]

    date_hierarchy = 'created_at'