from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.


def register(request):
    EDFO = DataForm()
    d = {'EDFO':EDFO}
    if request.method == "POST":
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        username = request.POST.get('username')
        password = request.POST.get('password')
        O1 = Data(name=name,pno=pno,email=email,add=add,username=username,password=password)
        O1.save()
        return HttpResponse('Registration Sucessfull')
    return render(request,'register.html',d)