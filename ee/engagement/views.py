from django.shortcuts import render, get_object_or_404, redirect
from engagement.models import Engagement, Staff
from employee.models import Employee
from django.views.generic import CreateView
from .forms import EngagementForm
from django.contrib import messages

# Create your views here.

#many to one - foreign key
#many to many - manytomanyfield

#a snippet of information of each engagement
def engagement_index(request):
    # import pdb; pdb.set_trace()
    engagement_list = Engagement.objects.all()   #the query
    




    employee_list = Employee.objects.all()






    if (request.method == 'POST') and ("addProj" in request.POST):
        form = EngagementForm(request.POST) #creating instance of the form
    
        if form.is_valid():
            import pdb; pdb.set_trace()
            form.save()

            title_in = request.POST.get('title')
            e1 = Engagement.objects.get(title=title_in)
            staff_list = request.POST.getlist('staff')                      #save the whole string of list of staff user input
            import pdb; pdb.set_trace()
            for x in staff_list:
                name_in, id_in = x.replace(")","").split(" (")               #split the strings 
                id_in = int(id_in)
                import pdb; pdb.set_trace()
                # staff_in = Staff(name=name_in, staff_id=id_in)              #build an object of staff with the inputs
                # staff_in.save()




                for e in employee_list:
                    if e.name == name_in and e.staffId == id_in:
                        staff_in = e
                import pdb; pdb.set_trace()






                e1.staff.add(staff_in)

            messages.success(request, f'{"Form submission successful"}')
            return redirect('engagement_index')                             #here should enter a new url where it will go if successful
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
