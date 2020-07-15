from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee, name="employee"),
    path("engagedProjects/", views.getEmployeeId, name='getEmployeeId'),
]