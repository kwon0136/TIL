from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Photo
#from django.conf import settings
from social_login.settings import *
import os

def login(request):
    users = User.objects.all()
    #if (request.user.is_authenticated):
     #   sa = request.user.socialaccount_set.all()
        #return redirect('upload')
    if request.method == "POST":
        return redirect('upload/')

    context = {'users':users}
    return render(request, 'login/login.html', context)

def upload(request):
    if request.method=="POST":

        #file = request.FILES.get('img_file')
        #title= request.POST.get('title')
        #msg= request.POST.get('message')
        if not os.path.exists(MEDIA_ROOT):
            os.mkdir(MEDIA_ROOT)
        path = os.path.join(MEDIA_ROOT, 'files')
        if not os.path.exists(path):
            os.mkdir(path)
        path2 = os.path.join(path, str(request.user.pk))
        if not os.path.exists(path2):
            os.mkdir(path2)

        for file in request.FILES.getlist('img_files'):
            p = Photo(photo=file, from_user=request.user)
            p.save()
            print(p.photo)
            print(p.message)

        if 'print' in request.POST:
            cbox_list = request.POST.getlist('cbox')
            for photo_pk in cbox_list:
                photo = Photo.objects.get(pk=photo_pk)
                photo.print = True
                photo.save()
                print(photo)
        elif 'sms' in request.POST:
            cbox_list = request.POST.getlist('cbox')
            for photo_pk in cbox_list:
                photo = Photo.objects.get(pk=photo_pk)
                photo.print = False
                photo.save()
                print(photo)



    photos = Photo.objects.filter(from_user=request.user)

    context= {'photos':photos}
    return render(request,'login/upload.html',context)