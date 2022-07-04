from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profilecreate/', views.profileCreate, name='profileCreate'),
    path('profilelist/', views.profileList, name='profileList'),
    path('moviedetail/', views.movieDetail, name='movieDetail'),
    path('movielist/', views.movieList, name='movieList'),
    path('show/', views.show, name='show'),
]
