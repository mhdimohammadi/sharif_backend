from django.urls import path
from . import views


app_name = "articles"



urlpatterns = [
    path("", views.articles, name="articles"),
    path("<int:pk>", views.article_detail, name="article_detail"),
    path("search_result", views.search_article, name="search_article"),
    path("post_comment", views.post_comment, name="post_comment"),

]