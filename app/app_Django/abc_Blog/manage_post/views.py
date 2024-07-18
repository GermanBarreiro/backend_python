from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Category, Rating
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
def rate_article(request, pk):
    vote = request.data.get('vote')
    if vote is not None:
        if isinstance(vote, str):  # Comprueba si vote es una cadena
            if vote.lower() in ['true', '1']:
                vote = True
            elif vote.lower() in ['false', '0']:
                vote = False
            else:
                vote = None  # Esto elimina el voto
        
        rating, created = Rating.objects.update_or_create(
            user_id=request.user,
            article_id_id=pk,
            defaults={'vote': vote},
        )
        return Response({'status': 'success', 'vote': rating.vote}, status=201)
    else:
        return Response({'status': 'error', 'message': 'Missing vote parameter'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
  print("Received data:", request.data)
  serializer = ArticleCreateSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user_id=request.user)  
    return Response(serializer.data, status=201)
  print("Validation errors:", serializer.errors)
  return Response(serializer.errors, status=400)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.filter(status=True)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)





