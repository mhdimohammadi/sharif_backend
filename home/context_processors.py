from home.models import HomeModel
from home.models import BannerModel

def site_settings(request):
    settings = HomeModel.objects.last()

    return {
        "site_settings": settings,
    }




def site_banners(request):
    banners = BannerModel.objects.last()

    return {
        "banners": banners,
    }