from django.urls import path
from Supermercado.views import *
from Supermercado.viewsFrontend import *
from Supermercado.viewsLogin import *
urlpatterns = [

    #URLS PARA EL BACKEND
    path('ADMINISTRATOR/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('ADMINISTRATOR/<str:AD_USER>',ADMINISTRATORView.as_view(),name='ListarAdministradorPorUsuario'),
    path('BUSINESS/',BUSINESSView.as_view(),name='ListarBusiness'),
    path('BUSINESS/<int:EM_nit>',BUSINESSView.as_view(),name='ListarBusiness'),
    path('EMPLOYEES/',EMPLOYEESView.as_view(),name='Listarempleados'),
    path('EMPLOYEES/<str:EMP_User>',EMPLOYEESView.as_view(),name='Listarempleadosporusuario'),
    path('Employeepayroll/',EMPLOYEEPAYROLLView.as_view(),name='Listarnomina'),
    path('Employeepayroll/<int:PAY_id>',EMPLOYEEPAYROLLView.as_view(),name='ListarID'),
    path('WORKINGHOURS/',EMPLOYEEPAYROLLView.as_view(),name='Listarhours'),
    path('WORKINGHOURS/<str:WORH_code>',EMPLOYEEPAYROLLView.as_view(),name='ListarHo'),
    path('CUSTOMERS/',CUSTOMERSView.as_view(),name='ListarCliente'),
    path('CUSTOMERS/<str:user>',CUSTOMERSView.as_view(),name='ListarClientePorUsuario'),
    path('LISTBUY/',LISTBUYView.as_view(),name='ListarListCompra'),
    path('LISTBUY/<str:LBUY_CLI_User_id>',LISTBUYView.as_view(),name='ListarPorCodigo'),
 
    path('EXPENSES/',EXPENSESView.as_view(),name='ListarEgresos'),
    path('EXPENSES/<str:code>',EXPENSESView.as_view(),name='BuscarEgresos'),
    path('INCOME/',INCOMEView.as_view(),name='ListarIngresos'),
    path('INCOME/<str:code>',INCOMEView.as_view(),name='BuscarIngresos'),
    path('PRODUCTS/',PRODUCTSView.as_view(),name='ListarProductos'),
    path('PRODUCTS/<int:PRO_Code>',PRODUCTSView.as_view(),name='BuscarProductos'),    


    #URLS PARA EL FRONTEND

    path('catalogo/',Catalogo,name="catalogo"),
    path('',index,name="index"),
    path('login/',login2,name="login"),
    
    path('ins_listCompra/',ins_listCompra,name="ins_listCompra"),
    path('listaCompra/',listCompra,name="listCompra"),
    path('listaCompra_eli/',listCompra_eli,name="listaCompra_eli"),
    path('ingresar/', iniciarsesion, name="ingresar"),
    path('cerrar/', cerrarsesion, name="cerrar"),

    # path('', principal, name="index"),
    path('MenuAdmin/', menuAdmin, name="MenuAdmin"),
    path('MenuEmpleado/', menuEmpleado, name="MenuEmpleado"),

    path('ListaClientes/', listaClientes, name='Lista'),
    path('BuscarCliente/', buscarCliente, name='Buscar'),
    path('FormCliente/', formRegistroCliente, name='Formulario'),
    path('RegistrarCliente/',registrarCliente, name='Registrar'),
    path('FormEditarCliente/<str:usuario>', formEditarCliente, name='Formulario2'),
    path('ActualizarCliente/',editarCliente, name='Actualizar'),
    path('EliminarCliente/<str:usuario>',eliminarCliente, name='Eliminar'),

    path('ListaClientesEMP/', listaClientesEMP, name='ListaClientesEMP'),
    path('BuscarClienteEMP/', buscarClienteEMP, name='BuscarClienteEMP')
    
    
]