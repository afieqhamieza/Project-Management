from django import forms
from .models import *

class EngagementForm(forms.ModelForm):
    title = forms.CharField(label="Project Title", required=False, widget=forms.TextInput( attrs={}) )
    body = forms.CharField(label="Project's Description", required=False, widget=forms.TextInput( attrs={}) )
    startDate = forms.CharField(label="Start Date yyyy-mm-dd", required=False, widget=forms.TextInput( attrs={}) )
    endDate = forms.CharField(label="End Date yyyy-mm-dd", required=False, widget=forms.TextInput( attrs={}) )
    staffId = forms.CharField(label="Engaged Employee", required=False, widget=forms.TextInput( attrs={}) )
    
    # clean start date
    def clean_start_date(self):
        data = self.cleaned_data['startDate']
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - date has passed'))
        # return the cleaned data.
        return data
    # end of clean start date function

    class Meta:
        model = Engagement
        fields = ('__all__')
