from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    # creating list of employee level
    level_list = "Associate", "Associate Director", "Assistant Manager", "Director", "Executive Director", "Manager", "Senior Associate"
    level_options = []

    for x in level_list:
        choice = (x, x)
        level_options.append(choice)

    name = forms.CharField(label="Employee Name", required=True, widget=forms.TextInput( attrs={}) )
    staffId = forms.IntegerField(label="Staff ID", required=True, widget=forms.TextInput( attrs={}) )
    level = forms.ChoiceField(label="Level", required=True, choices=level_options, widget=forms.Select(
        attrs={
            "style":' font-size: 14px;padding: 4px 4px;  display: block;  width: 300px;  height: 30px;  background-color: transparent;  border: none;  border-bottom: 1px solid #757575;'        }
    ) )
    team = forms.CharField(label="Team Name", required=True, widget=forms.TextInput( attrs={}) )

    class Meta:
        model = Employee
        fields = ('__all__') 
 