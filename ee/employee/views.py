from django.shortcuts import render
from employee.models import Employee

# Create your views here.

def employee(request):
    employee = Employee.objects.all()
    context = {
        'employees' : employee
    }

    return render(request, 'employee.html', context)