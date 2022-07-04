from django.urls import path
from . import views
app_name = 'app'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profilecreate/', views.profileCreate, name='profileCreate'),
    path('profilelist/', views.profileList, name='profileList'),
    path('moviedetail/', views.movieDetail, name='movieDetail'),
    path('movielist/', views.movieList, name='movieList'),
    path('show/', views.show, name='show'),
]
