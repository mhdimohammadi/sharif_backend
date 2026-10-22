from django.shortcuts import render
from articles.models import ArticleModel
from team.models import  TeamModel
from projects.models import ProjectModel
from home.models import IconModel
from our_service.models import ServiceModel
from django.db.models import Count,Q


def index(request):

    team_members = TeamModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:4]

    articles = ArticleModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:6]

    projects = ProjectModel.objects.filter(is_active=True)

    latest_projects = projects.order_by('-end_date')[:6]

    project_stats = projects.aggregate(
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

    icons = IconModel.objects.filter(
        is_active=True
    )

    services = ServiceModel.objects.all()[0:4]

    context = {
        "team_members": team_members,
        "articles": articles,
        "latest_projects": latest_projects,
        "icons": icons,
        "services": services,
        "done_projects_count": done_projects_count,
        "ongoing_projects_count": ongoing_projects_count,
    }

    return render(request,"index.html", context)