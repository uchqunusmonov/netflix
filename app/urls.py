from django.urls import path
from . import views
app_name = 'app'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profiles/', views.ProfileList.as_view(), name='profiles-list'),
    path('profile-create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('movie/<str:profile_id>/', views.MovieList.as_view(), name='movie-list'),
    path('movie/detail/<str:movie_id>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('movie/play/<str:movie_id>/', views.PlayMovie.as_view(), name='play-movie'),
]
