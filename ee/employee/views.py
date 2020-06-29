from django.shortcuts import render, get_object_or_404, redirect
from employee.models import Employee
from django.views.generic import CreateView
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.

def employee(request):
    employee = Employee.objects.all()

    if (request.method == 'POST') and ("addEmp" in request.POST):
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'{"Form Submission Successful"}')
            return redirect('employee')
    else:
        form = EmployeeForm()

    context = {
        'employees' : employee,
        'form': form,
    }
    
    return render(request, 'employee.html', context)

def load_levels(request):
    level_options = request.GET.get('')
    return render(request, 'employee.html', {'levels': level})