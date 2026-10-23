from django.shortcuts import render,redirect
from articles.models import CommentModel





def post_comment(request):
    if request.method == 'POST':
        data = request.POST
        author,text = data['author'],data['text']

        comment = CommentModel(
            author=author,text=text
        )
