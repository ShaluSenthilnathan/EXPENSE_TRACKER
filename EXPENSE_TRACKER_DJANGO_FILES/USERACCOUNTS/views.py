import re
from django.shortcuts import render,HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from USERACCOUNTS.models import *
from django.contrib.auth.forms import UserCreationForm
from USERACCOUNTS.forms import UserinfoTask,IncomesourcesTask

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 =  request.POST['password2']
        
        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
        
        
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ("/")  #calling home page
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login') #call the login page again
    
    else:
        return render(request,'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/') 


def enteroreditdata(request):
    return render(request,'enteroreditdata.html')


def enteruserinfo(request):
    if request.method == 'POST':
        form = UserinfoTask(request.POST or None)
        print("check1")
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('home')
    else:
        alldata = Userinfo.objects.all
        return render(request,'enteruserinfo.html',{'all_data':alldata})
    


def enterincomesources(request):
    if request.method == 'POST':
        form = IncomesourcesTask(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userid = Userinfo.user_id
            instance.save()
        return redirect('home')
    else:
        alldata = Incomesources.objects.all
        return render(request,'enterincomesources.html',{'all_data':alldata})

def entermonthlyexpenses(request):
    return render(request,'entermonthlyexpenses.html')
    
def viewdata(request):
    return render(request,'viewdata.html')

def viewuserdata(request):
    user =  Userinfo.objects.all
    return render(request,'viewuserdata.html',{'user':user})
