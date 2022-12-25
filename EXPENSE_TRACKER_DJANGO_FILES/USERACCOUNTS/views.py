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


def userinfo(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        usernname = request.POST.get('username')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        working_or_not = request.POST.get('working_or_not')
        print(userid,usernname)
        new_user = Userinfo(user_id=userid,username=usernname,gender=gender,age=age,email=email,phone_no=phone_no,working_or_not=working_or_not)
        new_user.save()
        print("data written")
        
    return render(request,'userinfo.html')


def incomesources(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        source_id = request.POST.get('source_id')
        monthly_income = request.POST.get('monthly_income')
        rental_income = request.POST.get('rental_income')
        intrest_amount = request.POST.get('intrest_amount')
        other_sources = request.POST.get('other_sources')
        total_cash = request.POST.get('total_cash')
        bank_balance = request.POST.get('bank_balance')
        net_amount = request.POST.get('net_amount')
        entry = Incomesources(userid=userid,source_id=source_id,monthly_income=monthly_income,rental_income=rental_income,intrest_amount=intrest_amount,other_sources=other_sources,total_cash=total_cash,bank_balance=bank_balance,net_amount=net_amount)
        entry.save()
        print("data2 written")
        
    return render(request,'incomesources.html')