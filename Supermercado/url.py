from django.urls import path
from Supermercado.views import *
urlpatterns = [
    path('ADMINISTRATOR/',ADMINISTRATORView.as_view(),name='ListarAdministrador'),
    path('ADMINISTRATOR/<str:dato>',ADMINISTRATORView.as_view(),name='ListarAdministradorPorUsuario'),
    path('Employeepayroll/',EMPLOYEEPAYROLLView.as_view(),name='Listarnomina'),
    path('Employeepayroll/<int:dato>',EMPLOYEEPAYROLLView.as_view(),name='ListarID'),
    path('WORKINGHOURS/',EMPLOYEEPAYROLLView.as_view(),name='Listarhours'),
    path('WORKINGHOURS/<str:dato>',EMPLOYEEPAYROLLView.as_view(),name='ListarHo'),
        
]