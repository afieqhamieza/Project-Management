from django.shortcuts import render
from engagement.models import Engagement
from employee.models import Employee
import datetime

# Create your views here.

def homepage(request):
    engagement_list = Engagement.objects.all()
    engagement_count = len(engagement_list)

    employee_list = Employee.objects.all()
    employee_count = len(employee_list)

    temp = list(reversed(engagement_list))
    latest7 = temp[:7]

    engagement_byEndDate = Engagement.objects.exclude(endDate__lte = datetime.date.today()).order_by('endDate', 'startDate')

    context= {
        'engCount': engagement_count,
        'empCount': employee_count,
        'latest7': latest7,
        'eng_byEndDate': engagement_byEndDate,
    }

    return render(request, 'homepage.html', context)