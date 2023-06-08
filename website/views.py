from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):
    records = Record.objects.all()




    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in.. ")
            return redirect('home')
    else:

        return render(request, 'home.html', {'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out..")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})


def prof_record1(request, pk):
    if request.user.is_authenticated:
        #look up record
        prof_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'prof_record':prof_record})

    else:
        messages.success(request,"You must be Logged In to view that page..")

        return redirect('home')



