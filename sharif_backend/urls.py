from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "پنل ادمین رایمند شریف"
admin.site.site_title = "پنل ادمین"
admin.site.index_title = "به پنل ادمین خوش آمدید"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls', namespace='home')),
    path('team/',include('team.urls', namespace='team')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)