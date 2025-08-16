
from members.models import registration
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User;
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
       
        my_user=User.objects.create_user(name,email,password)
        my_user.save()
        
        
    return render(request,"Fullstack.html")    

def en(request):
    if request.method=='POST':
        name=request.POST.get("name")
        pnumber=request.POST.get("pnumber")
        email=request.POST.get('email')
        b=registration(name=name,pnumber=pnumber,email=email)
        b.save()
    
    return render(request,"Fullstack(3)enqury_form.html")

def home1(request):
    if request.method=='POST':
        name=request.POST.get("username")
        pass1=request.POST.get("pass1")
        my_user1=authenticate(request, username=name, password=pass1)
        if my_user1 is not None:
            login(request, my_user1)
            return redirect("homes")
        else:
            return HttpResponse("Invalid")




    return render(request,"Fullstack(1).html")