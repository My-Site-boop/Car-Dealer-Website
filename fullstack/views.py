from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User;

def home(request):
    return render(request,"Fullstack.html")


def home2(request):
    return render(request,"Fullstack(2).html")


