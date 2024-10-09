from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

# Create your views here.

def index(request):
    return render(request,'testapp/index.html')

def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    #print(emp_list)
    return render(request,'testapp/emp.html',context=my_dict)
    #return HttpResponse('<h1>Sample response</h1>')