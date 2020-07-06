from django.shortcuts import render, get_object_or_404, redirect
from engagement.models import Engagement
from django.views.generic import CreateView
from .models import Engagement
from .forms import EngagementForm
from django.contrib import messages

# Create your views here.

#many to one - foreign key
#many to many - manytomanyfield

#a snippet of information of each engagement
def engagement_index(request):
    # import pdb; pdb.set_trace()
    engagement_list = Engagement.objects.all()   #the query

    if (request.method == 'POST') and ("addProj" in request.POST):
        form = EngagementForm(request.POST) #creating instance of the form
        # import pdb; pdb.set_trace()

        if form.is_valid():
            # import pdb; pdb.set_trace()
            # save user's input to the database here
            form.save()




            staff_input = request.POST.get('staff')
            import pdb; pdb.set_trace()
            #change the string in staff_input to fields of staff object
            #declare an instance of class
            form.staff.add(staff_input)
 





            messages.success(request, f'{"Form submission successful"}')
            return redirect('engagement_index')   #here should enter a new url where it will go if successful
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
