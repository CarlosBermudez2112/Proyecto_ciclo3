from django.urls import path
from Supermercado.views import *
urlpatterns = [
    path('ADMINISTRATOR/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('ADMINISTRATOR/<str:dato>',ADMINISTRATORView.as_view(),name='ListarAdministradorPorUsuario'),
    path('BUSINESS/',BUSINESSView.as_view(),name='ListarBusiness'),
    path('BUSINESS/<str:dato>',BUSINESSView.as_view(),name='ListarBusiness'),
    path('Employeepayroll/',EMPLOYEEPAYROLLView.as_view(),name='Listarnomina'),
    path('Employeepayroll/<int:dato>',EMPLOYEEPAYROLLView.as_view(),name='ListarID'),
    path('WORKINGHOURS/',EMPLOYEEPAYROLLView.as_view(),name='Listarhours'),
    path('WORKINGHOURS/<str:dato>',EMPLOYEEPAYROLLView.as_view(),name='ListarHo'),
    path('CUSTOMERS/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('CUSTOMERS/',CUSTOMERSView.as_view(),name='ListarCliente'),
    path('CUSTOMERS/<str:dato>',CUSTOMERSView.as_view(),name='ListarClientePorUsuario'),
        
]