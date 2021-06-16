from django.urls import path
from .views import AuthorView,ArticleView

urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('articles/', ArticleView.as_view()),
]