from django.contrib import admin
from home.models import AboutUsModel


@admin.register(AboutUsModel)
class HomeAdmin(admin.ModelAdmin):
    pass