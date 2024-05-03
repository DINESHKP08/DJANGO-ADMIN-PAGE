from django.shortcuts import render
from django.http import HttpResponse
from .models import data

# Create your views here.

def home(request):
    if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        contact = request.POST['contact']
        mail = request.POST['mail']

        obj = data()
        obj.Name=name
        obj.Age=age
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        mydata = data.objects.all()
        return render(request,'index.html',{'data':mydata})
    return render(request,'index.html')