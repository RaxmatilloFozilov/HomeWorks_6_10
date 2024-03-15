from django.urls import path
from django.views.generic import detail,list

from . import views

urlpatterns = [
    path('', views.pupils_list, name='pupils_list'),
    path('table/',views.table,name='table'),
    # path('<int:id>/', views.pupil_detail, name='pupil_detail'),
    # path('/', views.pupils_detail, name='pupil_dtail'),
    # path('detail', detail, name='detail'),
]


