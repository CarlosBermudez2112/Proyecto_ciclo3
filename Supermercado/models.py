from pyexpat import model
from django.db import models

# Create your models here.


## Creación de la tabla administradores junto con sus campos

class ADMINISTRATOR(models.Model):
    AD_USER=models.TextField(primary_key=True, max_length=50,null=False,unique=True)
    AD_PASSWORD=models.IntegerField(max_length=10)
    AD_EMAIL=models.TimeField(max_length=50,null=False)
    AD_NAMES=models.TextField(max_length=50,null=False)
    AD_LASTNAMES=models.TextField(max_length=50,null=False)
    AD_CELLPHONE=models.TextField(max_length=50,null=False)
    AD_ROL=models.TextField(max_length=50,null=False)

## Creación de la tabla empresas junto con sus campos

class BUSINESS(models.model):
    EM_ID=models.BigIntegerField(max_length=50,null=False)
    EM_IDName=models.TextField(max_length=50,null=False)
    EM_NIT=models.IntegerField(primary_key=True,max_length=10,unique=True)
    EM_CITY=models.TextField(max_length=50)
    EM_ADDRESS=models.TextField(max_length=50)
    EM_CELLPHONE=models.TextField(max_length=10)
    EM_DATECREATE=models.DateField()
    EM_PRODUCTIVE_SECTOR=models.TextField(max_length=50)
    EM_AD_USER=models.ForeignKey(ADMINISTRATOR,on_delete=models.CASCADE)
    
## Creación de la tabla empleados junto con sus campos

class EMPLOYEES(models.model):
    EMP_USER=models.TextField(primary_key=True,max_length=50,null=False,unique=True)
    EMP_PASSWORD=models.IntegerField(max_length=10)
    EMP_EMAIL=models.TimeField(max_length=50,null=False)
    EMP_NAMES=models.TextField(max_length=50,null=False)
    EMP_LASTNAMES=models.TextField(max_length=50,null=False)
    EMP_CELLPHONE=models.TextField(max_length=50,null=False)
    EMP_ROLE=models.TextField(max_length=50,null=False)
    EMP_EM_NIT=models.ForeignKey(BUSINESS,on_delete=models.CASCADE)
    EMP_AD_USER=models.ForeignKey(ADMINISTRATOR,on_delete=models.CASCADE)


class WORKINGHOURS(models.Model):
    WORH_Code=models.TextField(primary_key=True, max_length=50,null=True,unique=True)
    WORH_TipeHours=models.TextField(max_length=50,null=True,unique=True)
    WORH_Costs=models.IntegerField(null=True)
    
    
class EmployeePayroll(models.Model):
    PAY_Id=models.IntegerField(primary_key=True, auto_created=True, Unique=True)
    PAY_EM_User=models.ForeignKey(EMPLOYEES, on_delete=models.CASCADE)
    PAY_NIT=models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    PAY_Hours=models.IntegerField(null=True)
    PAY_ExtraHours=models.IntegerField(null=True)
    PAY_parafiscal=models.IntegerField(null=True)
    PAY_WorkingHours=models.ForeignKey(WORKINGHOURS, on_delete=models.CASCADE)
    PAY_StartDate=models.DateField()
    PAY_FinalDate=models.DateField()
    PAY_TotalSalary=models.IntegerField(null=True)

class CUSTOMERS(models.Model):
    CLI_User = models.TextField(primary_key=True, max_length=25,null=False,unique=True)
    CLI_Password=models.IntegerField(null=False)
    CLI_Email = models.EmailField(unique=True)
    CLI_Names = models.TextField(max_length=50,null=False)
    CLI_LastNames= models.TextField(max_length=50,null=False)
    CLI_CellPhone= models.TextField(max_length=50,unique=True)
    CLI_AD_User= models.ForeignKey(ADMINISTRATOR, on_delete=models.CASCADE)



class TypeExpenses(models.Model):
    TEGR_Code = models.CharField(primary_key=True, max_length=10,null=False,unique=True)
    TEGR_NameExpenses = models.IntegerField(max_length=10,null=False,unique=True)
    
class EXPENSES(models.Model):
    EGR_Code = models.CharField(primary_key=True, max_length=10,null=False,unique=True)
    EGR_EM_NIT = models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    EGR_TEGR_Code = models.ForeignKey(TypeExpenses, on_delete=models.CASCADE)
    EGR_Fecha = models.DateField(auto_now=True)
    EGR_Total = models.IntegerField(max_length=50,null=False)