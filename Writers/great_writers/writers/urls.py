from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writers/<str:name>', views.writers_Detail, name='writer_detail'),
    path('books/<str:name>/<str:book>', views.books, name='books'),
]




