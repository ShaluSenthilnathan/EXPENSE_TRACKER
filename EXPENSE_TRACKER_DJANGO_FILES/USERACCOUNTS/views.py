from django.shortcuts import render,HttpResponse 

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from USERACCOUNTS.models import *

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
        username = request.POST['username']
        password = request.POST['password']
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

#Going wrong - data input from forms to database 
def userinfo(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        usernname = request.POST['username']
        gender = request.POST['gender']
        age = request.POST['age']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        working_or_not = request.POST['working_or_not']
        print(userid,usernname)
        #new_user = userinfo(userid=userid,username=usernname,gender=gender,age=age,email=email,phone_no=phone_no,working_or_not=working_or_not)
        #new_user.save()
        print("data written")
        
    return render(request,'userinfo.html')