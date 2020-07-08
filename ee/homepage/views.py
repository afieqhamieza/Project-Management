from django.shortcuts import render
from engagement.models import Engagement
from employee.models import Employee

# Create your views here.

def homepage(request):
    engagement_list = Engagement.objects.all()
    engagement_count = len(engagement_list)

    employee_list = Employee.objects.all()
    employee_count = len(employee_list)

    context= {
        'engCount': engagement_count,
        'empCount': engagement_count
    }

    return render(request, 'homepage.html', context)