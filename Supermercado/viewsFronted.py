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


##Listar empleados

def ListarEmpleados(request):
    response=requests.get("http://127.0.0.1:8000/Supermercado/EMPLOYEES/")
    Empleados=response.json()    
    return render(request,"Empleados.html",Empleados)

## Buscra por user
def ListaDeEmpleadosuser(request):
    
    usuarioEmple=request.POST['EMP_USER']

    response=requests.get("http://127.0.0.1:8000/Supermercado/EMPLOYEES/"+usuarioEmple)
    Empleados=response.json()    
    print(Empleados)
    return render(request,"Empleados.html",Empleados)
##Eliminar empleados


def EliminarEmpleados(request,EMP_User):
    
    requests.delete("http://127.0.0.1:8000/Supermercado/EMPLOYEES/"+EMP_User)
   
    return redirect('../ListaDeEmpleados/')

##crear empleado
def CrearEmpleado(request):
    response=requests.get('http://localhost:8000/Supermercado/BUSINESS/')
    empresa = response.json()
    listaempresa = empresa
    #return render(request, "ingresoRegistrar.html",datos)
    print(listaempresa)
    return render (request,'FormularioEmpleado.html',listaempresa)

def GuardarEmpleado(request):
    datos={
      "EMP_USER": request.POST["IdUsuario"],
      "EMP_PASSWORD": request.POST["exampleInputPassword1"],
      "EMP_EMAIL":  request.POST["exampleInputEmail1"],
      "EMP_NAMES": request.POST["Nombre"],
      "EMP_LASTNAMES": request.POST["Apellidos"],
      "EMP_CELLPHONE": request.POST["Telefono"],
      "EMP_ROLE": "Empleado",
      "EMP_EM_NIT_id":request.POST["Empresa"],
      "EMP_AD_USER_id": "admin"
    }
    requests.post("http://127.0.0.1:8000/Supermercado/EMPLOYEES/",data=json.dumps(datos))
    
    return redirect("../ListaDeEmpleados/")


####actuzliaxr empleado

def FormularioActualizarEmpleado(request):
    response=requests.get('http://localhost:8000/Supermercado/BUSINESS/')
    empresa = response.json()
    listaempresa = empresa
    #return render(request, "ingresoRegistrar.html",datos)
    print(listaempresa)
    return render (request,'EditarFormularioEmpleado.html',listaempresa)

def EditarEmpleado(request):
    IdUsuario=request.POST["IdUsuario"]
    datos={
       
      "EMP_USER": request.POST["IdUsuario"] ,
      "EMP_PASSWORD": request.POST["exampleInputPassword1"],
      "EMP_EMAIL":  request.POST["exampleInputEmail1"],
      "EMP_NAMES": request.POST["Nombre"],
      "EMP_LASTNAMES": request.POST["Apellidos"],
      "EMP_CELLPHONE": request.POST["Telefono"],
      "EMP_ROLE": "Empleado",
      #"EMP_EM_NIT_id":request.POST["Empresa"],
      #"EMP_AD_USER_id": "admin"
    }
    requests.put("http://127.0.0.1:8000/Supermercado/EMPLOYEES/"+ IdUsuario,data=json.dumps(datos))
    
    return redirect("../ListaDeEmpleados/")