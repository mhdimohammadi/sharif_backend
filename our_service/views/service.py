from django.shortcuts import render
from our_service.models import ServiceModel




def service(request):
    services = ServiceModel.objects.all()

    return render(request,"services.html",{"services":services})