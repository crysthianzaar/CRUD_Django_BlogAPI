from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAdminUser, BasePermission
from .serializers import ArticleSerializer, AuthorSerializer
from .models import Author, Articles


class AuthorView(APIView):
    permission_classes = (BasePermission,)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        articles = Author.objects.all()
        serializer = AuthorSerializer(articles, many=True)
        return Response({"Author": serializer.data})
    

class ArticleView(APIView):
    permission_classes = (BasePermission,)
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})