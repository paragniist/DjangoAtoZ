from django.shortcuts import render
from . import forms

def Studentregisterview(req):
    form=forms.StudentRegistration()
    return render(req,'testapp/register.html',{'form':form})
