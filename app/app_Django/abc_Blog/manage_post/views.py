from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.filter(status=True)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk, status=True)
    except Article.DoesNotExist:
        return Response(status=404)
    
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)