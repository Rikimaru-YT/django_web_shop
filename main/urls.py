from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('shop/', views.shop_page, name='shop'),
    path('shop/detail/<int:product_id>/', views.show_product_detail, name='detail'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('search/', views.search, name='search'),

]