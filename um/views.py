from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Xuser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['pass1']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request,'home.html',{'error': "Invalid Credantials!"})
    else:
        return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':"Username has been alredy taken!"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['pass1'])
                phone = request.POST['phone']
                age = request.POST['age']
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                newXuser = Xuser(phone=phone,age=age,fname=fname,lname=lname,email=email,user=user)
                newXuser.save();
                auth.login(request,user)
                return redirect(show)
        else:
            return render(request,'register.htnl',{'error':"Password not match!"})
    else:
        return render(request,'register.html')


@login_required(login_url='/home/')
def show(request):
    datas = Xuser.objects.filter(user=request.user)
    return render(request,'show.html',{'data':datas})

def logout(request):
    auth.logout(request)
    messages.success(request,"You are successfully Logged Out!")
    return redirect(home)