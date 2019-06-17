from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.all()[::-1]
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context)

def new(request):
    if request.method == 'POST':
        movie = Movie()
        movie.title = request.POST.get('title')
        movie.title_origin = request.POST.get('title_origin')
        movie.vote_count = request.POST.get('vote_count')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/new.html')

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_origin = request.POST.get('title_origin')
        movie.vote_count = request.POST.get('vote_count')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        context = {'movie':movie}
        return render(request, 'movies/update.html', context)

def delete(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie_pk)