from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def insert_emp(request):
    LOE=Emp.objects.all()
    LOE=Emp.objects.filter(HIREDATE__year='1987')
    LOE=Emp.objects.filter(HIREDATE__month='2')
    LOE=Emp.objects.filter(HIREDATE__day='28')
    LOE=Emp.objects.filter(JOB__startswith='m')
    LOE=Emp.objects.filter(JOB__endswith='t')
    LOE=Emp.objects.filter(ENAME__contains='s')
    LOE=Emp.objects.filter(ENAME__in=('SMITH','BLAKE')) ## DOUBT
    LOE=Emp.objects.filter(Q(ENAME='SMITH') &  Q(JOB='CLERK'))
    LOE=Emp.objects.filter(Q(ENAME='BLAKE'))
    #LOE=Emp.objects.filter(ENAME__regex='[a-zA-Z]{7}')
    #LOE=Emp.objects.all()

    d={'data':LOE}
    return render(request,'display_emp.html',d)

