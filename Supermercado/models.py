from pyexpat import model
from django.db import models

# Create your models here.




class WORKINGHOURS(models.Model):
    WORH_Code=models.TextField(max_length=50,null=True,unique=True)
    WORH_TipeHours=models.TextField(max_length=50,null=True,unique=True)
    WORH_Costs=models.IntegerField(null=True)
    
    
class EmployeePayroll(models.Model):
    PAY_Id=models.IntegerField(auto_created=True, Unique=True)
    PAY_EM_User=models.ForeignKey(Employees, on_delete=models.CASCADE)
    PAY_NIT=models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    PAY_Hours=models.IntegerField(null=True)
    PAY_ExtraHours=models.IntegerField(null=True)
    PAY_parafiscal=models.IntegerField(null=True)
    PAY_WorkingHours=models.ForeignKey(WORKINGHOURS, on_delete=models.CASCADE)
    PAY_StartDate=models.DateField()
    PAY_FinalDate=models.DateField()
    PAY_TotalSalary=models.IntegerField(null=True)

class CUSTOMERS(models.Model):
    CLI_User = models.TextField(max_length=25,null=False,unique=True)
    CLI_Password=models.IntegerField(null=False)
    CLI_Email = models.EmailField(unique=True)
    CLI_Names = models.TextField(max_length=50,null=False)
    CLI_LastNames= models.TextField(max_length=50,null=False)
    CLI_CellPhone= models.TextField(max_length=50,unique=True)
    CLI_AD_User= models.ForeignKey(ADMINISTRATOR, on_delete=models.CASCADE)

class EXPENSES(models.Model):
    EGR_Code = models.CharField(10,null=False,unique=True)
    EGR_EM_NIT = models.ForeignKey(BUSINESS, on_delete=models.CASCADE)
    EGR_TEGR_Code = models.ForeignKey(TypeExpenses, on_delete=models.CASCADE)
    EGR_Fecha = models.DateField(auto_now=True)
    EGR_Total = models.IntegerField(max_length=50,null=False)

class TypeExpenses(models.Model):
    TEGR_Code = models.CharField(max_length=10,null=False,unique=True)
    TEGR_NameExpenses = models.IntegerField(max_length=10,null=False,unique=True)
    
    