from django.urls import path
from . import views

urlpatterns = [
    path("", views.engagement_index, name="engagement_index"),
    path("<int:pk>/", views.engagement_detail, name="engagement_detail"),
]