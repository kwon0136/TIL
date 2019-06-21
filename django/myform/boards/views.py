from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
       form = BoardForm(request.POST) # 사용자가 create.html에서 날린 데이터를
       #embed()
       if form.is_valid(): # form이 유효하면(is_vaild: 유효성 검사--> boolean값 리턴)
           board = form.save(commit=False) #commit=False: 저장 보류
           board.user = request.user #request.user: 로그인된 user 정보/ board.user: board class의 user field
           board.save()
           # title = form.cleaned_data.get('title') # .cleaned_data: 정제하여 dict 형태로
           # content = form.cleaned_data.get('content')
           # board = Board.objects.create(title=title, content=content) # .create(): .save() 필요없음
           return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    #board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk) # Board에 해당하는 pk있으면 가져오고, 없으면 404 error 띄운다
    person = get_object_or_404(get_user_model(), pk=board.user.pk)
    comments = board.comment_set.all()
    comment_form = CommentForm()
    context = {'board': board, 'comments':comments, 'comment_form':comment_form, 'person':person,}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method =='POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board_pk)
    else:
        return redirect('boards/index')

@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                form.save()
                # board.title = form.cleaned_data.get('title')
                # board.content = form.cleaned_data.get('content')
                # board.save()
                return redirect('boards:detail', board_pk)
        else:
            #form = BoardForm(initial=board.__dict__) # initial=board.__dict__: 초기값의 정보 제공/ board를 dict 형태로 전달
            form = BoardForm(instance=board)
    else:
        return redirect('boards:index')
    context = {'form':form, 'board':board}
    return render(request, 'boards/form.html', context)

@login_required
@require_POST # POST요청 이외의 요청이 들어오면 405 error 띄운다.
def comments_create(request, board_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # user 정보 필요하므로 잠시 hold
        comment.user = request.user # comment.user에 요청자의 정보를 넣는다
        comment.board_id = board_pk
        comment.save()
        return redirect('boards:detail', board_pk)

@login_required
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('boards:detail', board_pk)
    else:
        comment.delete()
        return redirect('boards:detail', board_pk)

@login_required
def like(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    user = request.user

    if request.user in board.like_users.all():
    # if board.like_users.filter(pk=user.pk).exists: # 최소 하나의 값이 들어가 있는지 확인/ 게시글에 좋아요를 누른 유저가 존재한다면
        board.like_users.remove(request.user) # 좋아요 또 누르면 좋아요 취소(like_user에서 제거)
    else:
        board.like_users.add(request.user) # 게시글에 좋아요를 누른 유저 존재X --> 좋아요 누르면 like_users에 추가
    return redirect('boards:index')

@login_required
def follow(request, board_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user in person.followers.all():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('boards:detail', board_pk)