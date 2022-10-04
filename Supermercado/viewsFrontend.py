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
    usu=request.POST['userPri']
    print(usu)
    dato={
        'LBUY_PRO_Code':int(request.POST['PRO_Code']),
        'LBUY_CLI_User':usu,
        'LBUY_Fecha':fecha
    }
    print(dato)
    requests.post("http://127.0.0.1:8000/Supermercado/LISTBUY/",data=json.dumps(dato))
    return redirect("../catalogo")

def listCompra(request,usuario):
       
    try:
        response=requests.get("http://127.0.0.1:8000/Supermercado/LISTBUY/"+usuario)
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
    except:
        return render(request,"ListCompra.html")
    

def listCompra_eli(request,usuario):
    LBUY_Code=request.POST['LBUY_Code']
    
    print(usuario)
    response=requests.delete('http://localhost:8000/Supermercado/LISTBUY/'+LBUY_Code)
   
       
    return redirect("../listaCompra/"+usuario)

def comprar(request,usuario):
    fecha=datetime.today()
    fecha=fecha.date()
    fecha=fecha.strftime('%yy-%m-%d')
    response=requests.get("http://127.0.0.1:8000/Supermercado/LISTBUY/"+usuario)
    jsond = json.loads(response.text)
    jsond=jsond['mensaje']
    
    
    for pro in jsond:
        dato={
            'LBUY_Fecha': fecha,
            'ING_Quantity':8000,
            'ING_Total': 1,
            'ING_EMP_User_id':"Dani456",
            'EM_nit':7984651,
            'ING_PRO_Code_id':int(pro.get('LBUY_PRO_Code_id'))      
        }
        response=requests.post('http://127.0.0.1:8000/Supermercado/INCOME/',data=json.dumps(dato))
        response=requests.delete('http://localhost:8000/Supermercado/LISTBUY/'+str(pro.get('LBUY_Code')))
    return redirect("../catalogo")


def menuAdmin(request):
    return render(request, "menuAdmin.html")

def menuEmpleado(request):
    return render(request, "menuEmpleado.html")

#METODOS PARA EL CRUD DE LA TABLA CLIENTES
def listaClientes(request):
    response = requests.get('http://localhost:8000/Supermercado/CUSTOMERS/')
    clientes = response.json()
    return render(request, "clientes.html", clientes)

def buscarCliente(request):
    dato = request.POST['usuario']
    response = requests.get('http://localhost:8000/Supermercado/CUSTOMERS/'+dato)
    cliente = response.json()
    return render(request, 'clientes.html', cliente)

def formRegistroCliente(request):
    response=requests.get('http://localhost:8000/Supermercado/ADMINISTRATOR/')
    userAdmin = response.json()
    return render(request, "clienteRegistrar.html", userAdmin)

def registrarCliente(request):
    datos={      
        "usuario": request.POST["usuario"],
        "password": request.POST["password"],
        "nombre": request.POST["nombre"],
        "apellido": request.POST["apellido"],
        "email": request.POST["email"],
        "telefono": request.POST["telefono"],
        "userAdmin": request.POST["userAdmin"]
    }
    requests.post('http://localhost:8000/Supermercado/CUSTOMERS/', data=json.dumps(datos))
    return redirect('../ListaClientes/')

def formEditarCliente(request, usuario):
    response=requests.get('http://localhost:8000/Supermercado/CUSTOMERS/'+usuario)
    cliente = response.json()
    return render(request, "clienteEditar.html", cliente)

def editarCliente(request):
    usuario= request.POST['usuario']
    datos={      
        "usuario": request.POST["usuario"],
        "password": request.POST["password"],
        "nombre": request.POST["nombre"],
        "apellido": request.POST["apellido"],
        "email": request.POST["email"],
        "telefono": request.POST["telefono"],
        "userAdmin": request.POST["userAdmin"]
    }
    # print(datos)
    requests.put('http://localhost:8000/Supermercado/CUSTOMERS/'+usuario, data=json.dumps(datos))
    return redirect('../ListaClientes/')

def eliminarCliente(request, usuario):
    requests.delete('http://localhost:8000/Supermercado/CUSTOMERS/'+usuario)
    return redirect('../ListaClientes/') 

def listaClientesEMP(request):
    response = requests.get('http://localhost:8000/Supermercado/CUSTOMERS/')
    clientes = response.json()
    return render(request, "clientesEMP.html", clientes)

def buscarClienteEMP(request):
    dato = request.POST['usuario']
    response = requests.get('http://localhost:8000/Supermercado/CUSTOMERS/'+dato)
    cliente = response.json()
    return render(request, 'clientesEMP.html', cliente)


#METODOS PARA EL CRUD DE LA TABLA INGRESOS
def listaIngresos(request):
    response = requests.get('http://localhost:8000/Supermercado/INCOME/')
    ingresos = response.json()
    return render(request, "ingresos.html", ingresos)

def buscarIngreso(request):
    dato = request.POST['codigo']
    response = requests.get('http://localhost:8000/Supermercado/INCOME/'+dato)
    ingreso = response.json()
    return render(request, 'ingresos.html', ingreso)

def formRegistroIngreso(request):
    response=requests.get('http://localhost:8000/Supermercado/EMPLOYEES/')
    empleado = response.json()
    response=requests.get('http://localhost:8000/Supermercado/BUSINESS/')
    empresa = response.json()
    response=requests.get('http://localhost:8000/Supermercado/PRODUCTS/')
    producto = response.json()
    datos = empresa|empleado|producto 
    return render(request, "ingresoRegistrar.html",datos)

def registrarIngreso(request):
    datos={  
        "Empresa":request.POST["empresa"],
        "Empleado": request.POST["empleado"],
        "Producto": request.POST["producto"],
        "ING_Quantity": request.POST["ING_Quantity"],
        "ING_Total": request.POST["ING_Total"]
    }
    requests.post('http://localhost:8000/Supermercado/INCOME/', data=json.dumps(datos))
    return redirect('../ListaIngresos/')

def formEditarIngreso(request, codigo):
    response=requests.get('http://localhost:8000/Supermercado/INCOME/'+codigo)
    ingreso = response.json()
    return render(request, "ingresoEditar.html", ingreso)

def editarIngreso(request):
    codigo= request.POST["codigo"]
    datos={
        "ING_Code": request.POST["codigo"],  
        "Empresa":request.POST['empresa'],
        "Empleado": request.POST["empleado"],
        "Producto": request.POST["producto"],
        "ING_Fecha": request.POST["fecha"],
        "ING_Quantity": request.POST["ING_Quantity"],
        "ING_Total": request.POST["ING_Total"]
    }
    requests.put('http://localhost:8000/Supermercado/INCOME/'+codigo, data=json.dumps(datos))
    return redirect('../ListaIngresos/')

def eliminarIngreso(request, codigo):
    requests.delete('http://localhost:8000/Supermercado/INCOME/'+codigo)
    return redirect('../ListaIngresos/') 


#METODOS PARA EL CRUD DE LA TABLA EGRESOS
def listaEgresos(request):
    response = requests.get('http://localhost:8000/Supermercado/EXPENSES/')
    egresos = response.json()
    return render(request, "egresos.html", egresos)

def buscarEgreso(request):
    dato = request.POST['codigo']
    response = requests.get('http://localhost:8000/Supermercado/EXPENSES/'+dato)
    egreso = response.json()
    return render(request, 'egresos.html', egreso)

def formRegistroEgreso(request):
    response=requests.get('http://localhost:8000/Supermercado/BUSINESS/')
    empresa = response.json()
    return render(request, "egresoRegistrar.html",empresa)

def registrarEgreso(request):
    datos={  
        "NIT_empresa":request.POST["NIT_empresa"],
        "EGR_Name": request.POST["EGR_Name"],
        "EGR_Total": request.POST["EGR_Total"]
    }
    requests.post('http://localhost:8000/Supermercado/EXPENSES/', data=json.dumps(datos))
    return redirect('../ListaEgresos/')

def formEditarEgreso(request, codigo):
    response=requests.get('http://localhost:8000/Supermercado/EXPENSES/'+codigo)
    egreso = response.json()
    return render(request, "egresoEditar.html", egreso)

def editarEgreso(request):
    codigo= request.POST["codigo"]
    datos={
        "EGR_Code": request.POST["codigo"],
        "NIT_empresa":request.POST["NIT_empresa"],
        "EGR_Name": request.POST["EGR_Name"],
        "EGR_Fecha": request.POST["EGR_Fecha"],
        "EGR_Total": request.POST["EGR_Total"]
    }
    requests.put('http://localhost:8000/Supermercado/EXPENSES/'+codigo, data=json.dumps(datos))
    return redirect('../ListaEgresos/')

def eliminarEgreso(request, codigo):
    requests.delete('http://localhost:8000/Supermercado/EXPENSES/'+codigo)
    return redirect('../ListaEgresos/') 
