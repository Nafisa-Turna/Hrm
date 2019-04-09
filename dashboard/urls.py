from django.urls import path
from . import views
urlpatterns =[
    path("login",views.hrmlogin,name='login'),
    path("logout",views.hrmlogout,name='logout'),
    path("",views.home,name="home"),
    path("dboard",views.dboard,name='dboard'),
    path("employee",views.employee,name='employee'),
    path("addemployee",views.addemployee,name='addemployee'),
    path("department",views.department,name='department'),
    path("attendance",views.attendance,name='attendance'),
    path("task",views.task,name='task'),
    path("holiday",views.holiday,name='holiday'),
    path("settings",views.settings,name='settings'),

]