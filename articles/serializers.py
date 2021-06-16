from rest_framework import serializers
from .models import Articles, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['category', 'author', 'title', 'summary','firstParagraph','body','status',]
