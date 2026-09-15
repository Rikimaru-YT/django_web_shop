from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('shop/', views.shop_page, name='shop'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('detail/', views.detail_page, name='detail'),
    path('cart/', views.cart_page, name='cart')
]