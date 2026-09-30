from home.models import HomeModel


def site_settings(request):
    settings = HomeModel.objects.last()

    return {
        "site_settings": settings,
    }