from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.engagement_index, name="engagement_index"),
    path("<int:pk>/", views.engagement_detail, name="engagement_detail"),
    path("editEngagement/", views.getengagementid, name='getengagementid'),
    path("getTeamEngaged/", views.getTeamEngaged, name='getTeamEngaged'),
    # path("getSelectedFilter/", views.getSelectedFilter, name='getSelectedFilter'),
    # path("updateEngagement/", views.updateEngagement, name='updateEngagement'),
    # path("updateTest/", views.updateTest, name='updateTest'),
    # url(r'element/update/(?P<pk>\d+)/$', 'views.engagement_index', name='engagement_index'),
]

# from django.shortcuts import redirect
# from .models import Element


# def getSelectedFilter(request):
#     # ...
#     element = Element.object.get(pk=1)
#     return redirect('element_update', pk=element.id)

#     temp1 = Engagement.object.get(pk=1)
#     return redirect('element_update', pk=element.id)

    

# def engagement_index(request, filter_in)