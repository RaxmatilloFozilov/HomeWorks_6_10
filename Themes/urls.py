from django.urls import path

from .views import  ThemesView,mavzu_1,mavzu_2,mavzu_3
from . import views

urlpatterns = [
    path('', ThemesView, name='ThemesView'),
    path('mavzu_1', mavzu_1, name='mavzu_1'),
    path('mavzu_2', mavzu_2, name='mavzu_2'),
    path('mavzu_3', mavzu_3, name='mavzu_3'),
    path('list', list, name='list'),
    path('', views.topic_list, name='topic_list'),
    path('<int:topic_id>/', views.topic_plans, name='topic_plans'),

]