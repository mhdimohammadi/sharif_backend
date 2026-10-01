from django.shortcuts import render
from team.models import TeamModel




def team_members(request):

    members = TeamModel.objects.filter(is_active=True).order_by('-priority')

    context = {
        'members': members,
    }

    return render(request,'team.html', context)