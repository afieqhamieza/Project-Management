from django.shortcuts import render
from engagement.models import Engagement

# Create your views here.

#a snippet of information of each engagement
def engagement_index(request):
    engagement = Engagement.objects.all()   #the query
    context = {     #context dictionary
        'engagements': engagement
    }
    
    return render(request, 'engagement_index.html', context)

#a detail view that shows more of information
def engagement_detail(request, pk):
    engagement = Engagement.objects.get(pk=pk)
    context= {
        'engagement': engagement
    }

    return render(request, 'engagement_detail.html', context)
