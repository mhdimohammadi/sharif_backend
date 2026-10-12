from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from projects.models import ProjectModel





def projects(request):

    _projects = ProjectModel.objects.filter(is_active=True)


    paginator = Paginator(_projects, 9)
    page_number = request.GET.get('page',1)

    try:
        _projects = paginator.page(page_number)
    except EmptyPage:
        _projects = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        _projects = paginator.page(1)



    context = {
        'projects': _projects,
    }

    return render(request, 'projects.html', context)






def project_detail(request, pk):

    try :
        project = ProjectModel.objects.get(pk=pk)

    except ObjectDoesNotExist :
        return redirect("home:index")


    context = {"project": project}

    return render(request,"project _details.html",context)