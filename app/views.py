from multiprocessing import context
import uuid
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie

class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:profiles-list')
        return render(request, 'index.html')


method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()

        context = {
            'profiles': profiles
        }

        return render(request, 'profileList.html', context)

method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profileCreate.html')
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('app:profiles-list')
        context = {
            'form': form
        }
        return render(request, 'profileCreate.html', context)


method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            last_movie = Movie.objects.filter(age_limit=profile.age_limit).order_by('-id')
            if profile not in request.user.profiles.all():
                return redirect('app:profiles-list')
            
            context = {
                'movies': movies,
                'last_movie': last_movie,
            }
            return render(request, 'movieList.html', context)
        except Profile.DoesNotExist:
            return redirect('app:profiles-list')


method_decorator(login_required, name='dispatch')
class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            context = {
                'movie': movie,
            }

            return render(request, 'movieDetail.html', context)
        except Movie.DoesNotExist:
            return redirect('app:movies-list')

method_decorator(login_required, name='dispatch')
class PlayMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            video = movie.video.values()
            context = {
                'video': list(video),
            }

            return render(request, 'showMovie.html', context)
        except Movie.DoesNotExist:
            return redirect('app:movies-list')