from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def iniciarsesion(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        data=request.POST['user_name']
        
        user_name = request.POST['user_name']
        password1 = request.POST['password']
        
       
        usu=User.objects.get(username=user_name)
        try:
          
            if usu is not None:
                
                if (usu.is_superuser==False and usu.is_staff==False):
                    login(request,usu)
                    
                    return render(request, "catalogo.html")
                if usu.is_superuser:
                    login(request,usu)
                    
                    #return render(request, "")
                if usu.is_staff:
                    login(request,usu)
                    
                    #return render(request, "")                    
        except usu==None:
            print("no existe")
                 

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def cerrarsesion(request):
    logout(request)
    return render(request, "catalogo.html")
