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

    article = get_object_or_404(
        ArticleModel.objects.select_related('author'),
        pk=pk,
        is_active=True,
    )

    latest_articles = (
        ArticleModel.objects
        .filter(is_active=True)
        .exclude(pk=article.pk)
        .only('title', 'cover_image', 'created_at')
        .order_by('-created_at')[:8]
    )


    context = {
        "article": article,
        "latest_articles": latest_articles,
    }

    return render(request,"blog_details.html",context)