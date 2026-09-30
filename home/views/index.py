from django.shortcuts import render
from home.models import HomeModel




def index(request):
    return render(request,"index.html")