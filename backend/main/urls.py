from django.urls import path
from .views import UserList, ProfilUserView, ProfilUpdateView, CreateUser, HobbiesUsersView, \
    HobbiesUsersUpdateView


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', ProfilUserView.as_view()),
    path('update/<int:pk>/', ProfilUpdateView.as_view()),
    path('hobbies/<int:pk>/', HobbiesUsersView.as_view()),
    path('hobbies_update/<int:pk>/', HobbiesUsersUpdateView.as_view()),
    path('register/', CreateUser.as_view()),

]