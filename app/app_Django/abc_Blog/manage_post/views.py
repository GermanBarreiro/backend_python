from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Category
from .serializers import ArticleListSerializer, ArticleDetailSerializer, ArticleCreateSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


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





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
  print("Received data:", request.data)
  serializer = ArticleCreateSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user=request.user)  
    return Response(serializer.data, status=201)
  print("Validation errors:", serializer.errors)
  return Response(serializer.errors, status=400)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.filter(status=True)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

