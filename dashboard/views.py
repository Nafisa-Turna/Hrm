from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from .models import*

# Create your views here.
def hrmlogin(request):
    if request.method=='GET':  
        return render(request,'dashboard/login.html')
    elif request.method=='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponseRedirect(reverse,("login"))

@login_required
def hrmlogout(request):
    logout(request)
    context = {
        'message' : 'Successfully logout'
    }
    return HttpResponseRedirect(reverse,('dashboard/login.html',context))

def dboard(request):
    return render(request,'dashboard/dboard.html')

def employee(request):
    return render(request,'dashboard/employee.html')


def addemployee(request):
    return render(request,'dashboard/addemployee.html')


def department(request):
    return render(request,'dashboard/department.html')


def attendance(request):
    return render(request,'dashboard/attendance.html')


def task(request):
    return render(request,'dashboard/task.html')

def holiday(request):
    return render(request,'dashboard/holiday.html')

def settings(request):
    return render(request,'dashboard/settings.html')

# @login_required
def home(request):
    return render(request,"dashboard/home.html")