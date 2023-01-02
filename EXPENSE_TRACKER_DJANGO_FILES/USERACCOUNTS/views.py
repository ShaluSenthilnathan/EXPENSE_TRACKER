from django.shortcuts import render,HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from USERACCOUNTS.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from USERACCOUNTS.forms import *

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
            messages.error(request,"Invalid Credentials")
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
        if form.is_valid():
            form.save()
            messages.success(request,("DATA SUCCESSFULY ADDED TO DATABASE"))
            return redirect('home')
        else:
            messages.error(request,form.errors)
            print(form.errors)
            return redirect('enteruserinfo')
    else:
        alldata = Userinfo.objects.all
        return render(request,'enteruserinfo.html',{'all_data':alldata})
        
        
def enterincomesources(request):
    if request.method == 'POST':
        form = IncomesourcesTask(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,form.errors)
            print(form.errors)
            return redirect('enterincomesources')
    else:
        alldata = Incomesources.objects.all
        return render(request,'enterincomesources.html',{'all_data':alldata})
    
def enterbankdata(request):
    if request.method == 'POST':
        form = BankdataTask(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,form.errors)
            print(form.errors)
            return redirect('enterbankdata')
    else:
        alldata = Bankdata.objects.all
        return render(request,'enterbankdata.html',{'all_data':alldata})
    
    
def entermonthlyexpenses(request):
    if request.method == 'POST':
        form = MonthlyExpensesTask(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,form.errors)
            print(form.errors)
            return redirect('entermonthlyexpenses')
    else:
        alldata = MonthlyExpenses.objects.all
        return render(request,'entermonthlyexpenses.html',{'all_data':alldata})
    
    
def viewdata(request):
    return render(request,'viewdata.html')

def viewuserdata(request):
    user1 =  Userinfo.objects.all
    return render(request,'viewuserdata.html',{'user1':user1})

def viewincomesourcesdata(request):
    user2 =  Incomesources.objects.all
    return render(request,'viewincomesources.html',{'user2':user2})

def viewmonthlyexpenses(request):
    user = MonthlyExpenses.objects.all
    return render(request,'viewmonthlyexpenses.html',{'user':user})

def viewbankdata(request):
    user4 = Bankdata.objects.all
    return render(request,'viewbankdata.html',{'user4':user4})