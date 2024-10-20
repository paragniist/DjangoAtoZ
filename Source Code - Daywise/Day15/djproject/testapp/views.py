from django.shortcuts import render
from testapp.models import * 

def index(request):
    return render(request,'testapp/index.html')

def hydjobs(request):
    hyd_list=Hydjobs.objects.order_by('date')
    my_dict={'hyd_list':hyd_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
    #return HttpResponse('<h1>Sample response</h1>')
    
def blrjobs(request):
        return render(request,'testapp/blrjobs.html')
    
def punejobs(request):
        return render(request,'testapp/punejobs.html')
    
