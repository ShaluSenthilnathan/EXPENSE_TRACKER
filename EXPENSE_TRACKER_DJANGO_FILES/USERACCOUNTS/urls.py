from django.contrib import admin
from django.urls import path,include 
from USERACCOUNTS import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'), 
    path('login',views.login,name='login'), 
    path('register',views.register,name='register'),
    path('logout',views.logout,name="logout"),
    path('enteroreditdata',views.enteroreditdata,name="enteroreditdata"),
    path('userinfo',views.userinfo,name='userinfo'),
    path('incomesources',views.incomesources,name='incomesources'),
]
