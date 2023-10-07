from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
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

def delete_record(request,pk):
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request,"Record Deleted Sucessfully...")
    return redirect('home')


from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import AddRecordForm

def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added..")
                return redirect('home')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('login')



    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been Updated!")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('login')