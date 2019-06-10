from django.shortcuts import render, redirect
from .models import Board

def index(request):

    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    # GET방식은 db에 접근이 가능하여 create에서 수정해도 수정된 글이 남게된다.
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 받아온 title, content를 DB에 저장
    # 1. from .models import Board 현재 디렉토리의 models.py에서 Board class import
    board = Board(title=title, contents=content)
    board.save()

    # redirect:
    return redirect(f'/boards/{board.pk}/')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, 'boards/edit.html', context)

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.contents = request.POST.get('contents')
    board.save()
    return redirect(f'/boards/{board.pk}/')