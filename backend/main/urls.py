from django.urls import path
from .views import UserList, ProfilUserView, ProfilUpdateView, CreateUser


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', ProfilUserView.as_view()),
    path('update/<int:pk>/', ProfilUpdateView.as_view()),
    path('register/', CreateUser.as_view()),

]