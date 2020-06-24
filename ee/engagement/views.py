from django.shortcuts import render
from engagement.models import Engagement
from django.views.generic import CreateView
from .models import Engagement
from .forms import EngagementForm

# Create your views here.

#a snippet of information of each engagement
def engagement_index(request):
    engagement = Engagement.objects.all()   #the query

    if request.method == 'POST':
        form = EngagementForm(request.POST)
        if form.is_valid():
            # should save user's input to the database here
            return HttpResponseRedirect()   #here should enter a new url where it will go if successful
    else: # means GET
        form = EngagementForm()
    
    context = {     #context dictionary
        'engagements':  engagement,
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

