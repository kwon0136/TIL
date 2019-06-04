from django.shortcuts import render
import requests
import random

def index(request):
    return render(request, 'utilites/index.html')

def photo(request):
    return render(request, 'utilites/photo.html')

