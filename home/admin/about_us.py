from django.contrib import admin
from home.models import FeatureModel,TimeLineModel


@admin.register(FeatureModel)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_editable = ['is_active']

@admin.register(TimeLineModel)
class TimeLineAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    list_editable = ['is_active']