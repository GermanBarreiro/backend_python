from django.contrib import admin
from django.urls import include, path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('manage_post.urls')),

    path('user/', include('user.urls')),
    path('login/', views.login),
    path('register/', views.Register),

]
