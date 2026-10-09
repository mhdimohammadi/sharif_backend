from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from articles.models import ArticleModel





def articles(request):

    _articles = ArticleModel.objects.filter(is_active=True)


    paginator = Paginator(_articles, 6)
    page_number = request.GET.get('page',1)

    try:
        _articles = paginator.page(page_number)
    except EmptyPage:
        _articles = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        _articles = paginator.page(1)



    context = {
        'articles': _articles,
    }

    return render(request, 'blog_grid.html', context)






def article_detail(request, pk):

    try :
        article = ArticleModel.objects.select_related('author').get(pk=pk)

    except ObjectDoesNotExist :
        return redirect("home:index")


    context = {"article": article}

    return render(request,"blog_details.html",context)