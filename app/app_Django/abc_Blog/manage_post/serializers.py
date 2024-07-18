from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Category, Rating
from .models import Category

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
            upvotes = ratings.filter(vote=True).count()
            total_votes = ratings.count()
            return upvotes / total_votes * 100  
        return 0

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user_id.username', read_only=True)
    categories = serializers.StringRelatedField(many=True)
    average_rating = serializers.SerializerMethodField()
    user_vote = serializers.SerializerMethodField()  # Nuevo campo

    class Meta:
        model = Article
        fields = ['id', 'title', 'introduction', 'body', 'image', 'author', 'categories', 'average_rating', 'user_vote', 'created', 'updated']  # Agregar 'user_vote' a los campos

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(article_id=obj, status=True)
        if ratings.exists():
            upvotes = ratings.filter(vote=True).count()
            total_votes = ratings.count()
            return upvotes / total_votes * 100  
        return 0
    def get_user_vote(self, obj):  # Método para obtener el voto del usuario actual
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            rating = Rating.objects.filter(user_id=request.user, article_id=obj).first()
            if rating:
                return rating.vote
        return None

class ArticleCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=True
    )

    class Meta:
        model = Article
        fields = ['title', 'introduction', 'body', 'image', 'categories']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
