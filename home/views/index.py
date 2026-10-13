from django.shortcuts import render
from articles.models import ArticleModel
from team.models import  TeamModel
from projects.models import ProjectModel



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

    context = {
        "team_members": team_members,
        "articles": articles,
        "projects": projects,
    }

    return render(request,"index.html", context)