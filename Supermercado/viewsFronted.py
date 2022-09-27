from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import json
from datetime import datetime

fecha=""
def Catalogo(request):
    response=requests.get("http://127.0.0.1:8000/Supermercado/PRODUCTS/")
    productos=response.json()    
    return render(request,"catalogo.html",productos)

def index(request):
    return render(request,"index.html")

def login2(request):
    print("1")
    return render(request,"login.html")

def ins_listCompra(request):
    fecha=datetime.today()
    fecha=fecha.date()
    fecha=fecha.strftime('%yy-%m-%d')
    usu="carlos"
    dato={
        'LBUY_PRO_Code':int(request.POST['PRO_Code']),
        'LBUY_CLI_User':usu,
        'LBUY_Fecha':fecha
    }
    print(dato)
    requests.post("http://127.0.0.1:8000/Supermercado/LISTBUY/",data=json.dumps(dato))
    return redirect("../catalogo")

def listCompra(request):
    response=requests.get("http://127.0.0.1:8000/Supermercado/LISTBUY/")
    lista=response.json()
     
    lista2=[]
    lista3={'mensaje':'a'}
    for lib in lista['mensaje']:
        response=requests.get("http://127.0.0.1:8000/Supermercado/PRODUCTS/"+str(lib["LBUY_PRO_Code_id"]))
        producto=response.json()
        producto=producto['mensaje']
        producto=producto[0]
        producto['LBUY_Code']=lib["LBUY_Code"]
        lista2.append(producto)
    lista3['mensaje']=lista2 
  
    return render(request,"ListCompra.html",lista3)

def listCompra_eli(request):
    LBUY_Code=request.POST['LBUY_Code']
    
    response=requests.delete('http://localhost:8000/Supermercado/LISTBUY/'+LBUY_Code)
   
    libro=response.json()
   
    return redirect('../listaCompra/')