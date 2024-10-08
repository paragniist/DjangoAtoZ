from django.shortcuts import render
import datetime 


def dateinfo(req):
    date=datetime.datetime.now()
    name='Nikhil!'
    msg=''
    h=int(date.strftime('%H'))
    if h<12:
        msg='Good morning!'
    elif h<16:
        msg='Good Afternoon!'
    elif h<22:
        msg='Good evening!'
    else:
        msg='Good Night!'
        
    my_dict={'date':date,'name':name,'msg':msg}
    return render(req,'testApp/dummy.html',context=my_dict)
