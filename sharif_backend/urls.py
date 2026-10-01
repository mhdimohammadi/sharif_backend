from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Raymand Sharif Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the admin panel"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls', namespace='home')),
    path('team/',include('team.urls', namespace='team')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)