from django.contrib import admin
from home.models import HomeModel


@admin.register(HomeModel)
class HomeAdmin(admin.ModelAdmin):
    pass