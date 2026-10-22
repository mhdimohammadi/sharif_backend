from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

from articles.models import ArticleModel


def search_article(request):

    query = request.GET.get('query', '').strip()
    queryset = ArticleModel.objects.filter(is_active=True)

    results = queryset.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )

    paginator = Paginator(results, 6)
    page_number = request.GET.get('page',1)

    try:
        results = paginator.page(page_number)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        results = paginator.page(1)

    context = {
        'results': results,
        'query': query,
    }

    return render(request, "search-result.html",context)