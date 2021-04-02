from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.


def index(request):
    return HttpResponse("Food Flix Alive")