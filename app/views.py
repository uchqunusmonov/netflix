from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

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



