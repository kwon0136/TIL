from django.shortcuts import render, redirect
from .models import Board


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    return redirect(f'/boards/{board.pk}/')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return redirect(f'/boards/{board.pk}')