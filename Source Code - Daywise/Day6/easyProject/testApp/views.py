from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    #s='<html><body><h1>Hello world of Django</h1></body></html>'
    return render(request,'testApp/hello.html')
    
