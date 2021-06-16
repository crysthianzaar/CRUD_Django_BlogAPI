from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAdminUser, IsAuthenticated, AllowAny 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ArticleSerializer, AuthorSerializer
from .models import Author, Articles

@permission_classes([IsAdminUser])
class AuthorView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        articles = Author.objects.all()
        serializer = AuthorSerializer(articles, many=True)
        return Response({"Author": serializer.data})
    
@permission_classes([IsAdminUser])
class ArticleView(APIView):
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)