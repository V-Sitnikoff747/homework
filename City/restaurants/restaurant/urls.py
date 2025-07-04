from django.urls import path
from . import views

urlpatterns =[

    path('', views.restaurant_list, name ="restaurant_list"),
    path('delete/<int:pk>/', views.delete_restaurant, name="delete_restaurant"),
    path('edit/<int:pk>', views.edit_restaurant, name='edit_restaurant'),
    path("search/", views.search_restaurants, name='search_restaurants'),
    path('add/', views.add_restaurant, name='add_restaurant'),
]   
