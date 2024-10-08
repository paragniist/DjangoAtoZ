from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='<h1> hi bro! Welcome to Django learning.'
    return HttpResponse(s) 


def logout(request):
    s='<h1> thanks for logging out.'
    return HttpResponse(s) 