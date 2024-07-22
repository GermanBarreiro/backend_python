from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index, name='index'),
    path('delete-account/', views.DeleteUserView.as_view(), name='delete_account'),
    path('update-profile/', views.UpdateUserView.as_view(), name='update_profile'),  
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
]