from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'newsapp/index.html')


def movies(req):
    head_msg='Latest movies info'
    msg1='Sonali marryiage'
    msg2='salman new release'
    msg3='Modi biopic in place'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(req,'newsapp/news.html',context=my_dict)

def sports(req):
    head_msg='Latest movies info'
    msg1='Sonali marryiage'
    msg2='salman new release'
    msg3='Modi biopic in place'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(req,'newsapp/news.html',context=my_dict)

def politics(req):
    head_msg='Latest politics info'
    msg1='Sonali marryiage'
    msg2='salman new release'
    msg3='Modi biopic in place'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(req,'newsapp/news.html',context=my_dict)

