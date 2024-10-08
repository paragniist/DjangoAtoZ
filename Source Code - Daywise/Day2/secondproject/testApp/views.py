from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h2> hi man good evening!! </h2><hr>'
    msg=msg+'<h1> server time is :'+str(date)+'</h1>'
    return HttpResponse(msg)

