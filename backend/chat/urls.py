from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room>/', views.room, name='room'),
]