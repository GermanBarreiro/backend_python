from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Category, Rating
from .serializers import (
    ArticleListSerializer, 
    ArticleDetailSerializer, 
    ArticleCreateSerializer, 
    CategorySerializer,
    ArticleSerializer
)

@api_view(['GET'])
@permission_classes([AllowAny])
def article_list(request):
    articles = Article.objects.filter(status=True)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk, status=True)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ArticleDetailSerializer(article, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_article(request, pk):
    vote = request.data.get('vote')
    if vote is not None:
        if isinstance(vote, str):
            if vote.lower() in ['true', '1']:
                vote = True
            elif vote.lower() in ['false', '0']:
                vote = False
            else:
                vote = None
        
        rating, created = Rating.objects.update_or_create(
            user_id=request.user,
            article_id_id=pk,
            defaults={'vote': vote},
        )
        return Response({'status': 'success', 'vote': rating.vote}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error', 'message': 'Missing vote parameter'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user_id=request.user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    categories = Category.objects.filter(status=True)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def modify_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user != article.user_id:
        return Response({"error": "You don't have permission to modify this article"}, 
                        status=status.HTTP_403_FORBIDDEN)
    
    serializer = ArticleSerializer(article, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)