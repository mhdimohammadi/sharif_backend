from django.shortcuts import render
from home.models import FeatureModel,TimeLineModel


def about_us(request):

    features = FeatureModel.objects.filter(is_active=True)
    timelines = TimeLineModel.objects.filter(is_active=True)

    context = {
        'features': features,
        'timelines': timelines,
    }

    return render(request,'aboutus.html',context)