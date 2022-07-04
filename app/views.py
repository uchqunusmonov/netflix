from django.shortcuts import redirect, render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'index.html')

def movieDetail(request):
    return render(request, 'movieDetail.html')

def movieList(request):
    return render(request, 'movieList.html')

def profileCreate(request):
    return render(request, 'profileCreate.html')

def profileList(request):
    return render(request, 'profileList.html')

def show(request):
    return render(request, 'showMovie.html')



