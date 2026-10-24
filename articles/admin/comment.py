from django.contrib import admin
from articles.models import CommentModel
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'is_active',
        'created_at'
    ]

    list_editable = ['is_active']
    search_fields = ['author', 'text']

    list_filter = [
        'is_active',
        ('created_at',JDateFieldListFilter),
        ('updated_at',JDateFieldListFilter),
    ]

    date_hierarchy = 'created_at'