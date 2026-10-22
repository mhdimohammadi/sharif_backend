from django.shortcuts import render
from django.db.models import Q,Count

from home.models import FeatureModel,TimeLineModel
from projects.models import ProjectModel

def about_us(request):

    features = FeatureModel.objects.filter(is_active=True)
    timelines = TimeLineModel.objects.filter(is_active=True)

    project_stats = ProjectModel.objects.filter(
        is_active=True
    ).aggregate(
        done_count=Count(
            'id',
            filter=Q(status=ProjectModel.Status.DONE)
        ),
        ongoing_count=Count(
            'id',
            filter=Q(status=ProjectModel.Status.ONGOING)
        ),
    )

    done_projects_count = project_stats['done_count']
    ongoing_projects_count = project_stats['ongoing_count']

    context = {
        'features': features,
        'timelines': timelines,
        "done_projects_count": done_projects_count,
        "ongoing_projects_count": ongoing_projects_count,
    }

    return render(request,'aboutus.html',context)