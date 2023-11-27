from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse("<h1>宇宙大战</h1>")



