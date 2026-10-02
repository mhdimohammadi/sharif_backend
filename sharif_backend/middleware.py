from django.shortcuts import render

from home.models import HomeModel


class SiteMaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site_setting = HomeModel.objects.last()

        if (
            site_setting
            and not site_setting.site_is_active
            and not request.path.startswith("/admin/")
        ):
            return render(
                request,
                "partials/maintenance.html",
                status=503,
            )

        return self.get_response(request)