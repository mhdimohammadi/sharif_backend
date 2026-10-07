from django.shortcuts import render
from home.models import FeatureModel


def about_us(request):

    features = FeatureModel.objects.filter(is_active=True)

    context = {
        'features': features
    }

    return render(request,'aboutus.html',context)