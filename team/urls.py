from django.urls import path
from . import views


app_name = "team"



urlpatterns = [
    path("members/", views.team_members, name="team_members"),

]