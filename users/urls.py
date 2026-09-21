from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.show_auth_page, name='auth'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('auth/logout/', views.user_logout, name='logout')
]
