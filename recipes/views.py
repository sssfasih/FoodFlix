from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request,'recipes/index.html')

def login(request):
    if request.method == "GET":
        return render(request,'recipes/login.html')
    else:return render(request,'recipes/login.html')

def signup(request):
    if request.method == "GET":
        return render(request,'recipes/signup.html')
    else:return render(request,'recipes/signup.html')

def drinks(request):
    return render(request,'recipes/drinks.html')