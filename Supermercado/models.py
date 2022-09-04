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
    
    