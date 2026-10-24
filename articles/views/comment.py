from django.shortcuts import redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages


from articles.models import CommentModel, ArticleModel





@require_POST
def post_comment(request):

    data = request.POST

    author = data['author']
    text = data['text']

    article_id = data['article_id']
    parent_id = data['parent_id']


    article = get_object_or_404(
        ArticleModel,
        pk=article_id,
    )

    if not author or not text:
        messages.error(
            request,
            "لطفاً تمام فیلدها را تکمیل کنید."
        )
        return redirect(
            'articles:article_detail',
            pk=article_id
        )

    parent = None

    if parent_id:
        parent = get_object_or_404(
            CommentModel,
            pk=parent_id,
            article=article,
            is_active=True,
        )

    CommentModel.objects.create(
        article=article,
        author=author,
        text=text,
        parent=parent,
    )

    messages.success(
        request,
        "کامنت شما با موفقیت ثبت شد و در صف بررسی قرار دارد."
    )

    return redirect(
        'articles:article_detail',
        pk=article_id
    )