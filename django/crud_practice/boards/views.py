from django.shortcuts import render,redirect
from .models import Board, Comment

def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def create(request):
    board = Board()
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:index')
    else:
        return render(request, 'boards/new.html')


def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    context = {'board':board, 'comments':comments}
    return render(request, 'boards/detail.html', context)

def update(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board_pk)
    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)


def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board_pk)

def comments_create(request, board_pk):
    comment = Comment()
    print(request.POST.get('content'))
    comment.content = request.POST.get('content')
    comment.board_id = board_pk
    comment.save()
    return redirect('boards:detail', board_pk)

def comments_update(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board_pk)
    else:
        context = {'comment': comment}
        return render(request, 'boards/comments_edit.html', context)


def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)