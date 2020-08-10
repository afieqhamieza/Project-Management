from django.shortcuts import render, get_object_or_404, redirect
from engagement.models import Engagement
from employee.models import Employee
from django.views.generic import CreateView
from .forms import EngagementForm
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.
filter_in = "highestEngagedMembers"

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
            staff_list = request.POST.getlist('staff')                       #save the whole string of list of staff user input

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
            print(form.errors)
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


    if (filter_in == "allProjects"):
        filteredEng = Engagement.objects.all() 
    elif (filter_in == "dueDate"):
        filteredEng = Engagement.objects.order_by('endDate')
    elif (filter_in == "completed"):
        filteredEng = Engagement.objects.filter(status = 'Completed')
    elif (filter_in == "projected"): 
        filteredEng = Engagement.objects.filter(status = 'Projected')
    elif (filter_in == "active"):
        filteredEng = Engagement.objects.filter(status = 'Active')
    elif (filter_in == "frozen"):
        filteredEng = Engagement.objects.filter(status = 'Frozen')
    elif (filter_in == "highestEngagedMembers"):
        filteredEng = Engagement.objects.annotate(highMem=Count('staff')).order_by('-highMem')
    else:
        filteredEng = engagement_list 

    # import pdb;pdb.set_trace()
    context = {     #context dictionary
        'engagements':  filteredEng,
        'form': form,
    }
    # import pdb;pdb.set_trace()
    return render(request, 'engagement_index.html', context)
       

def updateTest(request, pk):
    engagement_list = Engagement.objects.all()   
    employee_list = Employee.objects.all()

    specific_engagement = engagement_list.filter(id=pk_in)

    import pdb; pdb.set_trace()
    # if ("addProj" in request.POST):
    if (request.method == 'POST') and ("editProj" in request.POST):
        import pdb; pdb.set_trace()
        editform = EngagementForm(request.POST, instance=specific_engagement) #creating instance of the form

        if editform.is_valid():
            editform.save()

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
            print(editform.errors)
            messages.error(request, f'{"Form submission not valid - data not saved"}')
            context = {     #context dictionary
                'engagements':  engagement_list,
                'editform': editform,
            }
            return render(request, 'engagement_index.html', context)

            #instance 
            # re render balik
            #guna pk
            
    else: # means GET
        editform = EngagementForm(instance=specific_engagement)
    
    context = {     #context dictionary
        'engagements':  engagement_list,
        'editform': editform,
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
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        pk_in = request.POST.get("pk_in")

        #apply filter here to get the specific object   
        engagement_list = Engagement.objects.all()   
        specific_engagement = engagement_list.filter(id=pk_in)
        specific_eng_values= specific_engagement.values_list()
        eng=specific_eng_values[0]
        # import pdb; pdb.set_trace()
        # editform = EngagementForm(request.POST, instance=specific_engagement)
        results = { 
            "success":"True", 
            "project":eng, 
        }
        return JsonResponse(results)


def getTeamEngaged(request):
    if request.method == "POST":
        pk_in = request.POST.get("pk_in")

        #apply filter here to get the specific object   
        engagement_list = Engagement.objects.all()   
        specific_engagement = engagement_list.filter(id=pk_in)
        eng = specific_engagement[0]
        staffList = eng.staff.values() 

        nameList = []

        for temp in staffList:
            nameList.append(temp.get('name'))

        results = { "success":"True", "nameList":nameList }

        return JsonResponse(results)


# def getSelectedFilter(request):
#     filter_in = request.POST.get('filter_in')
#     engagement_list = Engagement.objects.all()

#     if (filter_in == "allProjects"):
#         filteredEng = engagement_list
#     elif (filter_in == "dueDate"):
#         filteredEng = Engagement.objects.order_by('endDate')
#     elif (filter_in == "completed"):
#         filteredEng = Engagement.objects.filter(status = 'Completed')
#     elif (filter_in == "projected"): 
#         filteredEng = Engagement.objects.filter(status = 'Projected')
#     elif (filter_in == "active"):
#         filteredEng = Engagement.objects.filter(status = 'Active')
#     elif (filter_in == "frozen"):
#         filteredEng = Engagement.objects.filter(status = 'Frozen')
#     elif (filter_in == "highestEngagedMembers"):
#         filteredEng = Engagement.objects.annotate(highMem=Count('staff')).order_by('-highMem')
#     else:
#         filteredEng = engagement_list


#     import pdb; pdb.set_trace()

#     fffilteredEng = list(filteredEng)
#     results = { 
#         "success":"True", 
#         "filteredEng": fffilteredEng
#     }
#     import pdb; pdb.set_trace()
#     return JsonResponse(results)


# def updateEngagement(request):
#     if request.method == "POST":
#         pk_in = request.POST.get("pk_in")
#         name_in = request.POST.get("name_in")
#         desc_in = request.POST.get("desc_in")
#         endDate_in = request.POST.get("endDate_in")
#         progress_in = request.POST.get("progress_in")
#         staff_in = request.POST.get("staff_in")

#         #apply filter here to get the specific object   
#         engagement_list = Engagement.objects.all()   
#         specific_engagement = engagement_list.filter(id=pk_in)
#         # specific_eng_values= specific_engagement.values_list()
#         eng = specific_engagement[0]
#         import pdb; pdb.set_trace()
#         eng.title = name_in

#         import pdb; pdb.set_trace()
        
#         results = { "success":"True" }
#         return JsonResponse(results)