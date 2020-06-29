from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    # creating list of employee level

    level_list = ["senior executive", "executive", "senior director", "director", "senior manager", "manager", "senior advisor", "advisor", "associate"]
    level_options = []

    for x in level_list:
        choice = (x[0], x[0])
        level_options.append(choice)


    name = forms.CharField(label="Employee Name", required=True, widget=forms.TextInput( attrs={}) )
    staffId = forms.IntegerField(label="Staff ID", required=True, widget=forms.TextInput( attrs={}) )
    level = forms.ChoiceField(label="Level", required=True, choices=level_options )
    team = forms.CharField(label="Team Name", required=True, widget=forms.TextInput( attrs={}) )

    class Meta:
        model = Employee
        fields = ('__all__')
