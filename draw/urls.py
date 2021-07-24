# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('home', views.home, name='home'),
    path('search1', views.search1, name='search1'),
    path('search2', views.search2, name='search2'),
    path('info', views.info, name='info'),
    path('upload_pic', views.upload_pic, name='upload_pic'),
    path('upload_description', views.upload_description, name='upload_description'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('food_info', views.food_info, name='food_info'),
    path('info', views.info, name='info'),

]
