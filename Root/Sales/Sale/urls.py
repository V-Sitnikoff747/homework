from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Покупатели
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),

    # Продавцы
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/add/', views.add_seller, name='add_seller'),

    # Товары
    path('products/', views.products, name='products'),
    path('products/add/', views.add_product, name='add_product'),
]


