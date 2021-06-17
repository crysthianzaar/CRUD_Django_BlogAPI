from django.urls import path
from .views import AuthorDetail,AuthorList, ArticleDetail, ArticleList


urlpatterns = [
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('authors/', AuthorList.as_view()),
    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>', ArticleDetail.as_view()),
]