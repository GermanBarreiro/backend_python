from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('delete-account/', views.DeleteUserView.as_view(), name='delete_account'),
    path('update-account/', views.UpdateUserView.as_view(), name='update_account'),
]