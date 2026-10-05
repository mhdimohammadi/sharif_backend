from django.shortcuts import render
from articles.models import ArticleModel
from team.models import  TeamModel




def index(request):

    team_members = TeamModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:4]

    articles = ArticleModel.objects.filter(
        is_active=True
    ).order_by('-priority')[:6]

    context = {
        "team_members": team_members,
        "articles": articles,
    }

    return render(request,"index.html", context)