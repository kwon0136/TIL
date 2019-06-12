from django.shortcuts import render, redirect
from .models import Board, Comment

def index(request):

    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, contents=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')

#def create(request):
#    # GET방식은 db에 접근이 가능하여 create에서 수정해도 수정된 글이 남게된다.
#    title = request.POST.get('title')
#    content = request.POST.get('content')
#
#    # 받아온 title, content를 DB에 저장
#    # 1. from .models import Board 현재 디렉토리의 models.py에서 Board class import
#    board = Board(title=title, contents=content)
#    board.save()
#
#    # redirect:
#    #return redirect(f'/boards/{board.pk}/')
#    return redirect('boards:detail', board.pk)

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)

    comments = board.comment_set.all()
    # comments = Comment.objects.filter(comment.board.pk=board_pk)
    context = {'board':board, 'comments':comments}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        #return redirect('/boards/')
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.contents = request.POST.get('contents')
        board.save()
        # return redirect(f'/boards/{board.pk}/')
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)

# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.contents = request.POST.get('contents')
#     board.save()
#     #return redirect(f'/boards/{board.pk}/')
#     return redirect('boards:detail', board.pk)

def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)

def comments_edit(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board_pk)
    else:
        context = {'comment':comment}
        return render(request, 'boards/comments_edit.html', context)

def comments_delete(request, board_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('boards:detail', board_pk)
    else:
        return redirect('boards:detail', board_pk)
