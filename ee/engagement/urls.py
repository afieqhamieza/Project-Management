from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.engagement_index, name="engagement_index"),
    path("<int:pk>/", views.engagement_detail, name="engagement_detail"),
    # url("/getengagementid/view/", name="getengagementid")
    # url(r'^/getengagementid/view/', views.getengagementid, name='getengagementid'),
    path("editEngagement/", views.getengagementid, name='getengagementid'),
]