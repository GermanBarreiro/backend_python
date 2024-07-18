from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='Categories',blank=False, null=False)
    slug=models.SlugField( unique=True,max_length=40)
    featured=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

class Article(models.Model):
    title=models.CharField(max_length=255)
    introduction=models.CharField(max_length=255)
    image=models.ImageField(upload_to='Articles',blank=False, null=False)
    body=models.TextField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"



class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    vote = models.BooleanField(null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user_id', 'article_id')  

    def __str__(self):
        if self.vote is None:
            return f'{self.user_id.username} - No vote'
        return f'{self.user_id.username} - {"Upvote" if self.vote else "Downvote"}'