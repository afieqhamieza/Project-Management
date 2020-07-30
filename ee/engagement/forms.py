from django import forms
from .models import *
from employee.models import Employee

class EngagementForm(forms.ModelForm):
    # creating list of staff options
    staff_list = Employee.objects.values_list('name')    
    id_list = Employee.objects.values_list('staffId')              
    staff_options = [('','')]

    for x in range(len(staff_list)):
        name = staff_list[x]    #tuple
        id = str(id_list[x][0])     #tuple
        name_id = ''.join(name) + " (" + ''.join(id) + ")"   #string
        choice = (name_id, name_id)     #tuple if buat (  ,  )
        staff_options.append(choice)
    # import pdb; pdb.set_trace()
    status_options=[
        ('',''),
        ("Proposed", "Proposed"),
        ("Active", "Active"),
        ("Completed", "Completed"),
        ("Frozen", "Frozen"),
        ("Projected", "Projected"),
    ]
        

    title = forms.CharField(label="Project Title", required=True, widget=forms.TextInput( attrs={}) )
    body = forms.CharField(label="Project's Description", required=True, widget=forms.TextInput( attrs={}) )
    startDate = forms.DateField(label="Start Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    endDate = forms.DateField(label="End Date yyyy-mm-dd", required=True, widget=forms.TextInput( attrs={}) )
    staff = forms.MultipleChoiceField(label="Engaged Employee", required=False, choices=staff_options)
    status = forms.ChoiceField( required=True, choices=status_options, widget=forms.Select(
        attrs={
            "style":'font-size: 18px; padding: 10px 10px 10px 5px; display: block; width: 300px; border: none; border-bottom: 1px solid #757575;'
        }
    ))

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
        exclude = [ 'progress', 'staff' ]
