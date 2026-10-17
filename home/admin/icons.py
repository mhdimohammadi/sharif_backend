from django.contrib import admin
from home.models import IconModel


@admin.register(IconModel)
class IconAdmin(admin.ModelAdmin):
    list_display = ['priority','is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']
