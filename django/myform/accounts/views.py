from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from  .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth import update_session_auth_hash

def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = UserCustomCreationForm()
    context = {'form':form}
    return render(request, 'accounts/auth_forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST) # request: 요청정보, form.get_user():user정보
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'boards:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login2.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('boards:index')
    else:
        return redirect('boards:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:index')

def edit(request):
    if request.method == 'POST':
        #form = UserChangeForm(request.POST, instance=request.user)
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        #form = UserChangeForm(instance=request.user)
        form = UserCustomChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_forms.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST ) # request.user: 요청자의 정보, request.POST: 기존 비밀번호, 변경된 비밀번호,
        if form.is_valid():
            #form.save()
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_forms.html', context)