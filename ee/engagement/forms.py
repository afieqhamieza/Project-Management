from django import forms
from .models import *
from employee.models import Employee

class EngagementForm(forms.ModelForm):
    staff_options = Employee.objects.values_list('name')                  
    staff_list = []
    
    for x in staff_options:
        choice = (x[0], x[0])
        staff_list.append(choice)
        

    title = forms.CharField(label="Project Title", required=True, widget=forms.TextInput( attrs={}) )
    body = forms.CharField(label="Project's Description", required=True, widget=forms.TextInput( attrs={}) )
    startDate = forms.DateField(label="Start Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    endDate = forms.DateField(label="End Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    # staffId = forms.IntegerField(label="Engaged Employee", required=True, widget=forms.TextInput( attrs={}) )
    # staff = forms.ChoiceField(label="Engaged Employee", required=True, choices=staff_list)
    staff = forms.MultipleChoiceField(label="Engaged Employee", required=True, choices=staff_list)

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
        exclude = [ 'status', 'progress' ]
