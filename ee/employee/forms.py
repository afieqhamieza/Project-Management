from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    name = forms.CharField(label="Employee Name", required=True, widget=forms.TextInput( attrs={}) )
    staffId = forms.IntegerField(label="Staff ID", required=False, widget=forms.TextInput( attrs={}) )
    level = forms.CharField(label="Level", required=True, widget=forms.TextInput( attrs={}) )
    team = forms.CharField(label="Team Name", required=True, widget=forms.TextInput( attrs={}) )

    class Meta:
        model = Employee
        fields = ('__all__')
