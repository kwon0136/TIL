from django.shortcuts import render
from .models import Board

def index(request):

    board = Board.objects.all()
    context = {'board':board}
    return render(request, 'boards/index.html', context)

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 받아온 title, content를 DB에 저장
    # 1. from .models import Board 현재 디렉토리의 models.py에서 Board class import
    board = Board(title=title, contents=content)
    board.save()

    return render(request, 'boards/create.html')