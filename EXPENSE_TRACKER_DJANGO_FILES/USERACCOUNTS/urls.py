from django.contrib import admin
from django.urls import path,include 
from USERACCOUNTS import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'), 
    
    path('login',views.login,name='login'), 
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    
    path('enteroreditdata',views.enteroreditdata,name='enteroreditdata'),
    path('enteruserinfo',views.enteruserinfo,name='enteruserinfo'),
    path('enterincomesources',views.enterincomesources,name='enterincomesources'),
    path('entermonthlyexpenses',views.entermonthlyexpenses,name='entermonthlyexpenses'),
    path('enterbankdata',views.enterbankdata,name='enterbankdata'),
    
    path('viewdata',views.viewdata,name='viewdata'),
    path('viewuserdata',views.viewuserdata,name='viewuserdata'),
    path('viewincomesources',views.viewincomesourcesdata,name='viewincomesources'),
    path('viewmonthlyexpenses',views.viewmonthlyexpenses,name='viewmonthlyexpenses'),
    path('viewbankdata',views.viewbankdata,name='viewbankdata'),
    path('viewexpensescategory',views.viewexpensescategory,name='viewexpensescategory'),
]
