from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from .models import*
from .forms.department import *

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
            return HttpResponseRedirect(reverse("login"))

@login_required
def hrmlogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return HttpResponseRedirect(reverse('login'))

@login_required
def dboard(request):
    return render(request,'dashboard/dboard.html')

@login_required
def employee(request):
    return render(request,'dashboard/employee.html')

@login_required
def addemployee(request):
    return render(request,'dashboard/addemployee.html')

@login_required
def department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('department'))
    else:
        form = DepartmentForm()
    department_data = Department.objects.all()
    context={
            'department_data': department_data,
            'form' : form
        }
    return render(request, 'dashboard/department.html',context)

@login_required
def depdelete(request, pk):
    Department.objects.filter(pk=pk).delete()
    messages.info(request, 'Delete post')
    return HttpResponseRedirect(reverse('department'))

@login_required
def depupdate(request,pk):
    data=get_object_or_404(Department,pk=pk)
    if request.method == 'POST':
        form=DepartmentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department'))
    else:    
        form = DepartmentForm(instance=data)
        context={
            'form':form
        }
    return render(request,'dashboard/editdepartment.html',context)
@login_required
def attendance(request):
    return render(request,'dashboard/attendance.html')

@login_required
def task(request):
    return render(request,'dashboard/task.html')

@login_required
def holiday(request):
    return render(request,'dashboard/holiday.html')

@login_required
def settings(request):
    return render(request,'dashboard/settings.html')

@login_required
def home(request):
    return render(request,"dashboard/home.html")