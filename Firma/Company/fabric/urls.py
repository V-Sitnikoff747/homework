from django.urls import path, re_path
from . import views

urlpatterns= [

    path('', views.home, name='home'),
    re_path(r'^news.*', views.news, name='news'),
    re_path(r'^management.*', views.management, name='management'),
    re_path(r'^about.*', views.about, name='about'),
    re_path(r'^contacts.*', views.contacts, name='contacts'),
    re_path(r'^branches/?$', views.branches, name='branches'),
    re_path(r'^branches/(?P<city>\w+)$', views.branch_detail, name='branch_detail'),   
]
