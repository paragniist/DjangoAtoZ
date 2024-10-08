from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish1(req):
    return HttpResponse('<h1>This is first App !!!</h1>')