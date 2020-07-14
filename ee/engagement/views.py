from django.shortcuts import render, get_object_or_404, redirect
from engagement.models import Engagement
from employee.models import Employee
from django.views.generic import CreateView
from .forms import EngagementForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

#a snippet of information of each engagement
def engagement_index(request):
    engagement_list = Engagement.objects.all()   
    employee_list = Employee.objects.all()

    
    if (request.method == 'POST') and ("addProj" in request.POST):
        form = EngagementForm(request.POST) #creating instance of the form
    
        if form.is_valid():
            form.save()

            title_in = request.POST.get('title')
            e1 = Engagement.objects.get(title=title_in)
            staff_list = request.POST.getlist('staff')                      #save the whole string of list of staff user input

            for x in staff_list:
                name_in, id_in = x.replace(")","").split(" (")               #split the strings 
                id_in = int(id_in)

                for emp in employee_list:
                    if emp.name == name_in and emp.staffId == id_in:
                        staff_in = emp

                e1.staff.add(staff_in)

            messages.success(request, f'{"Form submission successful"}')
            return redirect('engagement_index')                             #here should enter a new url where it will go if successful
    
        else:
            messages.error(request, f'{"Form submission not valid - data not saved"}')
            context = {     #context dictionary
                'engagements':  engagement_list,
                'form': form,
            }
            return render(request, 'engagement_index.html', context)

            #instance 
            # re render balik
            #guna pk


    
    else: # means GET
        form = EngagementForm()
    
    context = {     #context dictionary
        'engagements':  engagement_list,
        'form': form,
    }
    return render(request, 'engagement_index.html', context)


#a detail view that shows more of information
def engagement_detail(request, pk):
    engagement = Engagement.objects.get(pk=pk)
    context= {
        'engagements': engagement
    }

    return render(request, 'engagement_detail.html', context)


def getengagementid(request):
    if request.method == "POST":
        pk_in = request.POST.get("pk_in")

        #apply filter here to get the specific object   
        engagement_list = Engagement.objects.all()   
        specific_engagement = engagement_list.filter(id=pk_in)
        xx= specific_engagement.values_list()
        yy=xx[0]

        results = { "success":"True", "project":yy }
        import pdb; pdb.set_trace()
        return JsonResponse(results)
