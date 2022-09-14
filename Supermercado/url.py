from django.urls import path
from Supermercado.views import *
urlpatterns = [
    path('ADMINISTRATOR/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('ADMINISTRATOR/<str:AD_USER>',ADMINISTRATORView.as_view(),name='ListarAdministradorPorUsuario'),
    path('BUSINESS/',BUSINESSView.as_view(),name='ListarBusiness'),
    path('BUSINESS/<int:EM_nit>',BUSINESSView.as_view(),name='ListarBusiness'),
    path('Employeepayroll/',EMPLOYEEPAYROLLView.as_view(),name='Listarnomina'),
    path('Employeepayroll/<int:PAY_id>',EMPLOYEEPAYROLLView.as_view(),name='ListarID'),
    path('WORKINGHOURS/',EMPLOYEEPAYROLLView.as_view(),name='Listarhours'),
    path('WORKINGHOURS/<str:WORH_code>',EMPLOYEEPAYROLLView.as_view(),name='ListarHo'),
    path('CUSTOMERS/',CUSTOMERSView.as_view(),name='ListarCliente'),
    path('CUSTOMERS/<str:user>',CUSTOMERSView.as_view(),name='ListarClientePorUsuario'),
    path('LISTBUY/',LISTBUYView.as_view(),name='ListarListCompra'),
    path('LISTBUY/<int:LBUY_code>',LISTBUYView.as_view(),name='ListarPorCodigo'),
    path('TYPEEXPENSES/',TYPEEXPENSESView.as_view(),name='ListarTiposCobros'),
    path('TYPEEXPENSES/<str:code>',TYPEEXPENSESView.as_view(),name='ListarTipoCobros'),    

]