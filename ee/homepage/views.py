from django.shortcuts import render
from engagement.models import Engagement

# Create your views here.

def homepage(request):

    return render(request, 'homepage.html', {})