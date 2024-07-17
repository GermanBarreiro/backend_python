from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Rating

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user_id.username')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'average_rating']

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(article_id=obj, status=True)
        if ratings.exists():
            return sum(rating.values for rating in ratings) / ratings.count()
        return 0

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user_id.username')
    categories = serializers.StringRelatedField(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'body', 'image', 'author', 'categories', 'average_rating', 'created', 'updated']

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(article_id=obj, status=True)
        if ratings.exists():
            return sum(rating.values for rating in ratings) / ratings.count()
        return 0