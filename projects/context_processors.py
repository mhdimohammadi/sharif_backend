from projects.models import ProjectModel




def latest_projects(request):
    projects = ProjectModel.objects.all().order_by('-end_date')[:4]

    return {
        "latest_projects": projects,
    }