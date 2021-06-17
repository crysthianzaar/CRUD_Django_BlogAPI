from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import  IsAdminUser, IsAuthenticated, AllowAny 
from rest_framework import status, generics
from django.http import Http404
from .serializers import ArticleSerializer, AuthorSerializer
from .models import Author, Articles


@permission_classes([IsAdminUser])
class AuthorDetail(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsAdminUser])
class AuthorList(APIView):
    def get(self, request, format=None):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminUser])
class ArticleList(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    model = Articles
    serializer_class = ArticleSerializer

    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminUser])
class ArticleDetail(APIView):

    def get_object(self, slug):
        try:
            return Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        articles = self.get_object(slug)
        serializer = ArticleSerializer(articles)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        articles = self.get_object(slug)
        serializer = ArticleSerializer(articles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        articles = self.get_object(slug)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
