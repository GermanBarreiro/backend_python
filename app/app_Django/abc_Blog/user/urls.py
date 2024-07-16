from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('', views.index, name='index'),
]