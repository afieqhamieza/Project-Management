from django.shortcuts import render, get_object_or_404, redirect
from employee.models import Employee
from django.views.generic import CreateView
from engagement.models import Engagement
from .forms import EmployeeForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def employee(request):
    employee_list = Employee.objects.all()

    if (request.method == 'POST') and ("addEmp" in request.POST):
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'{"Form Submission Successful"}')
            return redirect('employee')
    else:
        form = EmployeeForm()

    context = {
        'employees' : employee_list,
        'form': form,
    }
    
    return render(request, 'employee.html', context)

#get the id of specific employee to get list of engagements
def getEmployeeId(request):
    if request.method == "POST":
        pk_in = request.POST.get("pk_in")

        #apply filter here to get the specific object   
        employee_list = Employee.objects.all()
        specific_employee = employee_list.filter(id=pk_in)

        engagedProjectList = []
        yy = specific_employee[0].engagement_set.all()

        for temp in yy:
            engagedProjectList.append(temp.title)

        results = { "success":"True", "projectList":engagedProjectList }
        return JsonResponse(results)