from django import forms
from .models import *

class EngagementForm(forms.ModelForm):
    title = forms.CharField(label="Project Title", required=False,widget=forms.TextInput(
        attrs={
                "placeholder":" Project's title",
                'class':'target',
        }))
    body = forms.CharField(label="Project's Description", required=False, widget=forms.TextInput(
        attrs={
                "placeholder":"Project's Description",
        }))
    startDate = forms.CharField(label="Start Date yyyy/mm/dd", required=False, widget=forms.TextInput(
        attrs={
                "placeholder":"Start Date yyyy/mm/dd",
        }))
    endDate = forms.CharField(label="End Date yyyy/mm/dd", required=False, widget=forms.TextInput(
        attrs={
                "placeholder":"End Date yyyy/mm/dd",
        }))
    staffId = forms.CharField(label="Engaged Employee", required=False, widget=forms.TextInput(
        attrs={
                "placeholder":"Engaged Employee",
        }))
    

    class Meta:
        model = Engagement
        fields = ('__all__')
