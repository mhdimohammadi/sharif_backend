from django.contrib import admin
from home.models import HomeModel,BannerModel


@admin.register(HomeModel)
class HomeAdmin(admin.ModelAdmin):
    pass



@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    pass
