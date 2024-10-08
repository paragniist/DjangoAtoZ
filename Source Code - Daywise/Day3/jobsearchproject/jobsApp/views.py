from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hydjobs(request):
    s='Hyderabad Jobs info'
    return HttpResponse(s)

def punejobs(request):
    s='Pune Jobs info'
    return HttpResponse(s)

def banglorejobs(request):
    s='banglore Jobs info'
    return HttpResponse(s)

def chennaijobs(request):
    s='<h1>Chennai Jobs info</h1>'
    return HttpResponse(s)
