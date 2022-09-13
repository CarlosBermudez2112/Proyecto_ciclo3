#from django.shortcuts import render
from ast import Delete
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Supermercado.models import *
from django.http import JsonResponse


class ADMINISTRATORView(View):
    ##consultar administradores
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,AD_USER=""):
        if len(AD_USER)>0:
            UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
            if len(UserAdmin)>0:
                datos={"mensaje":UserAdmin}
            else:
                datos={'mensaje: No se encontro administrador'}
        else:
            UserAdmin =list(ADMINISTRATOR.objects.values())
        if len(UserAdmin)>0:
            datos={"mensaje":UserAdmin}
        else:
            datos={'mensaje: no se encontro Ningun administrador registrado'}

        return JsonResponse(datos)
    
    ##crear administrador
    
    def post(self,request):
        data=json.loads(request.body) 
        Admin=ADMINISTRATOR(AD_USER=data['AD_USER'],AD_PASSWORD=data['AD_PASSWORD'],AD_EMAIL=data['AD_EMAIL']
                             , AD_NAMES=data[' AD_NAMES'],AD_LASTNAMES=data['AD_LASTNAMES'],
                             AD_CELLPHONE=data['AD_CELLPHONE'],AD_ROL=data['AD_ROL'])
        Admin.save()
        datos={'Mensaje': 'Administrador registrado exitosamente'}
        return JsonResponse(datos)
    
    ##Actualizar administrador

    def put(self,request,AD_USER):
        data=json.loads(request.body) 
        UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
        if len(UserAdmin)>0:
            admin=UserAdmin.objects.get(AD_USE=AD_USER)
            admin.AD_PASSWORD=data['AD_PASSWORD']
            admin.AD_EMAIL=data['AD_EMAIL']
            admin.AD_NAMES=data[' AD_NAMES']
            admin.AD_LASTNAMES=data['AD_LASTNAMES']
            admin. AD_CELLPHONE=data['AD_CELLPHONE']
            admin.AD_ROL=data['AD_ROL']
            admin.save()
            datos={'Mensaje': 'Administrador actualizado exitosamente'}
        else :
            datos={'Mensaje': 'Administrador no encontrado para actualizar'}
        return JsonResponse(datos)
        
    ##Borrar administrador
    
    def delete(self,request,AD_USER):
        UserAdmin =list(ADMINISTRATOR.objects.filter(AD_USE=AD_USER).values())
        if len(UserAdmin)>0:
           UserAdmin.objects.filter(AD_USE=AD_USER).delete()
           datos={'Mensaje': 'Administrador eliminado exitosamente'}
        else :
            datos={'Mensaje': 'Administrador no encontrado para eliminar'}
        return JsonResponse(datos)


class BUSINESSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,EM_ID=""):
        if len(EM_ID)>0:
            Business=list(BUSINESS.objects.filter(EM_ID=EM_ID).values())
            if len(Business)>0:
                datos={"mensaje":Business}
            else:
                datos={"mensaje":"no hay empresas registradas con ese Id"}
        else:
            Business=list(BUSINESS.objects.values())
            if len(Business)>0:
                datos={"mensaje":Business}
            else:
                datos={"mensaje":"no hay empresas registradas"}
        return JsonResponse(datos)
    
     
class EMPLOYEEPAYROLLView(View):
     #metodos para utilisar json
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,PAY_id=None):
        if len(PAY_id)>0:
            payemplo=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).values())
            if len(payemplo)>0:
                datos={"mensaje":payemplo}
            else:
                datos={"mensaje":"no hay datos"}
        else:
            payemplo=list(EMPLOYEEPAYROLL.objects.values())
            if len(payemplo)>0:
                datos={"mensaje":payemplo}
            else:
                datos={"mensaje":"no hay datos"}
        return JsonResponse(datos)
        
    def post(self,request):
        try:
            dat=json.loads(request.body)
            #llaves foraneas
            emp=EMPLOYEES.objects.get(EMP_USER=dat['emp_user'])
            em_nit=BUSINESS.objects.get(EM_NIT=dat['em_nit1'])
            worh_code=WORKINGHOURS.objects.get(WORH_Code=dat['worh_code1'])
            
            
            #creación de json para enviar
            
            newemployeepayroll=EMPLOYEEPAYROLL.objects.create(emp_user=emp,
                                                              em_nit1=em_nit,
                                                              PAY_Hours=dat['PAY_Hours'],
                                                              PAY_ExtraHours=dat['PAY_ExtraHours'],
                                                              PAY_parafiscal=dat['PAY_parafiscal'],
                                                              worh_code1=worh_code,
                                                              PAY_StartDate=dat['PAY_StartDate'],
                                                              PAY_FinalDate=dat['PAY_FinalDate'],
                                                              PAY_TotalSalary=dat['PAY_TotalSalary'])
            newemployeepayroll.save()
            datos={'mensaje':'nomina registrada'}
        
        except EMPLOYEES.DoesNotExist:
            datos={'mensaje':'el empleado no existe'}
        except BUSINESS.DoesNotExist:
            datos={'mensaje':'la empresa no existe'}
        except WORKINGHOURS.DoesNotExist:
            datos={'mensaje':'ese estilo de hora no es posible ingresarla'}
        return JsonResponse(datos)
        
    def put(self,request,PAY_id):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        emp=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(emp)>0:
            empPay=emp.objects.get(PAY_Id=PAY_id)
            empPay.PAY_EM_User=data["PAY_EM_User"]
            empPay.PAY_NIT=data["PAY_NIT"]
            empPay.PAY_Hours=data["PAY_Hours"]
            empPay.PAY_ExtraHours=data["PAY_ExtraHours"]
            empPay.PAY_parafiscal=data['PAY_parafiscal']
            empPay.PAY_WorkingHours=data["PAY_WorkingHours"]
            empPay.PAY_StartDate=data["PAY_StartDate"]
            empPay.PAY_FinalDate=data["PAY_FinalDate"]
            empPay.PAY_TotalSalary=data["PAY_TotalSalary"]
            empPay.save()
            
            mensaje={"mensaje":"se a actualizado la nomida requerida"}
        else:
            mensaje={"mensaje":"no existe la nomida requerida"}
        return JsonResponse(mensaje)
        
    def delete(self,request,PAY_id):
        
        PAY_id=list(EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).values())
        if len(PAY_id)>0:
            EMPLOYEEPAYROLL.objects.filter(PAY_Id=PAY_id).delete()
            mensaje={"mensaje":"se a eliminado el registro"}
        else:
            mensaje={"mensaje":"no existe el dato, no se elimino nada"}
        return JsonResponse(mensaje)
        
class WORKINGHOURSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,WORH_code=""):
        if len(WORH_code)>0:
            worhours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
            if len(worhours)>0:
                datos={"mensaje":worhours}
            else:
                datos={"mensaje":"no hay datos"}
        else:
            worhours=list(WORKINGHOURS.objects.values())
            if len(worhours)>0:
                datos={"mensaje":worhours}
            else:
                datos={"mensaje":"no hay datos"}
        return JsonResponse(datos)
    
    def post(self,request):
        try:
            dat=json.loads(request.body)
        
            #creación de json para enviar
            
            newemployeepayroll=EMPLOYEEPAYROLL.objects.create(WORH_Code=dat['WORH_Code'],
                                                              WORH_TipeHours=dat['WORH_TipeHours'],
                                                              WORH_Costs=dat['WORH_Costs'])
                                                              
            newemployeepayroll.save()
            datos={'mensaje':'hora registrada'}
        
        except:
            datos={'mensaje':'no se registro'}
        return JsonResponse(datos)
    
    def put(self,request,WORH_code):
        #crear conexion a body
        data=json.loads(request.body)
        #genero la busqueda con el dato
        hours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
        #genero la busqueda si hay valores con el dato de busqueda anterior
        if len(hours)>0:
            hor=hours.objects.get(WORH_Code=WORH_code)
            hor.WORH_TipeHours=data["PAY_EM_User"]
            hor.WORH_Costs=data["PAY_NIT"]                        
            mensaje={"mensaje":"se a actualizado la hora requerida"}
        else:
            mensaje={"mensaje":"no existe la hora requerida"}
        return JsonResponse(mensaje)
    
    def delete(self,request,WORH_code):
        #data=json.loads(request.body)
        hours=list(WORKINGHOURS.objects.filter(WORH_Code=WORH_code).values())
        if len(hours)>0:
            WORKINGHOURS.objects.filter(WORH_Code=WORH_code).delete()
            mensaje={"mensaje":"se a eliminado la hora"}
        else:
            mensaje={"mensaje":"no existe el dato, no se elimino nada"}
        return JsonResponse(mensaje)
        
class CUSTOMERSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Metodo para leer datos
    def get(self,request,user=""):
        #Se verifica si user tiene datos.
        if len(user)>0:   
            clientes= list(CUSTOMERS.objects.filter(CLI_User=user).values())
            if len(clientes)>0:
                #Se muestra el cliente con el user que se ha especificado
                mensaje = {'mensaje':clientes}
            else:
                mensaje = {'mensaje': "No se encontro el cliente."}
        else:
            clientes= list(CUSTOMERS.objects.values()) 
            if len(clientes)>0:#se pregunta si hay datos
                #Se muestra todos los clientes existentes en la BD
                mensaje={"mensaje":clientes}
            else:
                mensaje={"mensaje":"No se encontraron clientes."}

        return JsonResponse(mensaje)

    #Metodo para insertar un dato
    def post(self,request):
        dato = json.loads(request.body) #Trae todo el objeto que viene con la petición, para posterior insertar en la tabla
        userAdmin=ADMINISTRATOR.objects.get(AD_USER=dato['user_Admin'])
        cliente = CUSTOMERS.objects.create(
            CLI_User=dato['usuario'], 
            CLI_AD_User=userAdmin,
            CLI_Password=dato['password'],
            CLI_Names=dato['nombre'],
            CLI_LastNames=dato['apellido'], 
            CLI_Email=dato['email'],
            CLI_Cellphone=dato['telefono']
            )
        cliente.save()
        mensaje={'mensaje':'Cliente registrado exitosamente'}
        
        return JsonResponse(mensaje)

    #Metodo para actualizar un dato 
    def put(self,request,user):
        data = json.loads(request.body)
        cliente= list(CUSTOMERS.objects.filter(CLI_User=user).values())
        if len(cliente)>0:
            #NOTA:
            #No es necesario actualizar todos los datos, solo los que especifiquemos en este condicional.
            updateData=CUSTOMERS.objects.get(CLI_User=user) #Se trae el objeto que se encontró
            updateData.CLI_Password=data['password']
            updateData.CLI_Names=data['nombre']
            updateData.CLI_LastNames=data['apellido'] 
            updateData.CLI_Email=data['email']
            updateData.CLI_Cellphone=data['telefono']
            updateData.save()
            mensaje={"mensaje":"Cliente actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el cliente."}
            
        return JsonResponse(mensaje)

    #Metodo para borrar un dato
    def delete(self,request,user):
        cliente= list(CUSTOMERS.objects.filter(CLI_User=user).values())
        if len(cliente)>0:
            CUSTOMERS.objects.filter(CLI_User=user).delete()
            mensaje={"mensaje":"Cliente eliminado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el Cliente."}
        
        return JsonResponse(mensaje)


class TYPEEXPENSESView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,code=""):
        if len(code)>0:   
            tipoCobros= list(TYPEEXPENSES.objects.filter(TEGR_Code=code).values())
            if len(tipoCobros)>0:
                mensaje = {'mensaje':tipoCobros}
            else:
                mensaje = {'mensaje': "No se encontro el tipo de cobro indicado."}
        else:
            tipoCobros= list(TYPEEXPENSES.objects.values()) 
            if len(tipoCobros)>0:
                mensaje ={"mensaje":tipoCobros}
            else:
                mensaje ={"mensaje":"No se encontraron los tipos de cobros."}

        return JsonResponse(mensaje)

    def post(self,request):
            data = json.loads(request.body) #Trae todo el objeto que viene con la petición, para posterior insertar en la tabla
            tipoCobro = TYPEEXPENSES(
                TEGR_Code=data['codigo_tipo_cobro'], 
                TEGR_NameExpenses=data['nombre_cobro']
                )
            tipoCobro.save()
            mensaje={'mensaje':'Tipo de cobro registrado exitosamente'}
            return JsonResponse(mensaje)

    def put(self,request,code):
        data = json.loads(request.body)
        tipoCobro= list(TYPEEXPENSES.objects.filter(TEGR_Code=code).values())
        if len(tipoCobro)>0:
            #NOTA:
            #No es necesario actualizar todos los datos, solo los que especifiquemos en este condicional.
            updateData=TYPEEXPENSES.objects.get(TEGR_Code=code) #Se trae el objeto que se encontró
            updateData.TEGR_NameExpenses=data['nombre_cobro']          
            updateData.save()
            mensaje={"mensaje":"Tipo de cobro actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el tipo de cobro indicado."}
            
        return JsonResponse(mensaje)

    def delete(self,request,code):
        tipoCobro= list(TYPEEXPENSES.objects.filter(TEGR_Code=code).values())
        if len(tipoCobro)>0:
            TYPEEXPENSES.objects.filter(TEGR_Code=code).delete()
            mensaje={"mensaje":"Tipo de cobro eliminado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el tipo de cobro indicado."}
        
        return JsonResponse(mensaje)
    


   