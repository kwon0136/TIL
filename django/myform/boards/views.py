from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm
from IPython import embed


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == 'POST':
       form = BoardForm(request.POST) # 사용자가 create.html에서 날린 데이터를
       #embed()
       if form.is_valid(): # form이 유효하면(is_vaild: 유효성 검사--> boolean값 리턴)
           board = form.save()
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
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method =='POST':
        board.delete()
        return redirect('boards:index')
    return redirect('boards:detail', board_pk)

def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
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
    context = {'form':form, 'board':board}
    return render(request, 'boards/form.html', context)