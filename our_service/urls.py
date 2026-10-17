from django.urls import path
from . import views


app_name = "our_service"



urlpatterns = [
    path("/our_services", views.service, name="service"),
]