from rest_framework import serializers
from .models import Articles, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id','category', 'author', 'title', 'summary','firstParagraph','body','status',]
