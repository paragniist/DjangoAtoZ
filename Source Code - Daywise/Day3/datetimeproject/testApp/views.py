from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def datetimeinfo(request):
    date=datetime.datetime.now()
    dt=int(date.strftime("%H"))
    msg='<h1> Hello people!! '
    if dt<12:
        msg=msg+'Good morning'
    elif dt<16:
        msg=msg+'Good Afternoon'
    elif dt<20:
        msg=msg+'Good evening'
    else:
        msg=msg+'Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h2>Current time is:'+str(date)+'</h2>'
    
    return HttpResponse(msg)