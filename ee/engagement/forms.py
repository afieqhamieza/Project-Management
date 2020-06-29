from django import forms
from .models import *
from employee.models import Employee

class EngagementForm(forms.ModelForm):
    # creating list of staff options
    staff_list = Employee.objects.values_list('name')                  
    staff_options = []

    for x in staff_list:
        choice = (x[0], x[0])
        staff_options.append(choice)
        

    title = forms.CharField(label="Project Title", required=True, widget=forms.TextInput( attrs={}) )
    body = forms.CharField(label="Project's Description", required=True, widget=forms.TextInput( attrs={}) )
    startDate = forms.DateField(label="Start Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    endDate = forms.DateField(label="End Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    # staffId = forms.IntegerField(label="Engaged Employee", required=True, widget=forms.TextInput( attrs={}) )
    # staff = forms.ChoiceField(label="Engaged Employee", required=True, choices=staff_list)
    staff = forms.MultipleChoiceField(label="Engaged Employee", required=True, choices=staff_options)

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
