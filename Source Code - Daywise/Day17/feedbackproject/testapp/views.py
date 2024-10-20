from django.shortcuts import render
from . import forms 

# Create your views here.

def feedback_view(req):
    form=forms.FeedbackForm()
    if req.method=='POST':
        form=forms.FeedbackForm(req.POST)
        if form.is_valid():
            print('Validation success & print info')
            print('Student Name: ',form.cleaned_data['name'])
            print('Student Rollno: ',form.cleaned_data['rollno'])                       # print('Student Name: ',form.cleaned_data['name'])
            print('Student Mail id: ',form.cleaned_data['email'])
            print('Student Feedback: ',form.cleaned_data['feedback'])
        else:
            print('Invalid data')
            return render(req,'testapp/thanks.html') #,{'name':form.cleaned_data['name']})
    return render(req,'testapp/feedback.html',{'form':form})

