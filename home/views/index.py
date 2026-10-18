from django.shortcuts import render
from articles.models import ArticleModel
from team.models import  TeamModel
from projects.models import ProjectModel
from home.models import IconModel
from our_service.models import ServiceModel

def index(request):

    team_members = TeamModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:4]

    articles = ArticleModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:6]

    projects = ProjectModel.objects.filter(
        is_active=True
    ).order_by('-end_date')[:6]

    icons = IconModel.objects.filter(
        is_active=True
    )

    services = ServiceModel.objects.all()[0:4]

    context = {
        "team_members": team_members,
        "articles": articles,
        "projects": projects,
        "icons": icons,
        "services": services,
    }

    return render(request,"index.html", context)