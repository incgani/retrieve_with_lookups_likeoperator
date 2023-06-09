from django.db import models

# Create your models here.
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100,unique=True)
    LOC=models.CharField(max_length=100)
    def __str__(self):
        return str(self.DEPTNO)
    
class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField(null=True)
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMN=models.IntegerField(null=True)
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ENAME