from django.shortcuts import render
from team.models import  TeamModel




def index(request):

    team_members = TeamModel.objects.filter(is_active=True).order_by('-priority')[:4]

    context = {
        "team_members": team_members
    }

    return render(request,"index.html", context)