from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop-detail/<int:id>/', views.shop_detail, name='shop-detail'),
    path('buy-product/<int:id>/', views.buy_product, name='buy-product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('filter/<str:category>/', views.filter_view, name='filter'),
    path('search/', views.search_view, name='search'),
]
