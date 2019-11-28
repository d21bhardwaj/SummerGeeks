from django import forms
from .models import *

class EntryForm(forms.ModelForm): 
    
    class Meta:
        model = Entry
        exclude = ['in_time', 'out_time','left_office','verification']
        widgets = {
            'visitor_title' : forms.Select(attrs = {'class': 'regDropDown'}),
            'visitor_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'visitor_phone_no' : forms.TextInput(attrs={'class': 'form-control'}),
            'visitor_email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'host_name' : forms.Select(attrs = {'class': 'regDropDown'}),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['host_name'].queryset = Employee.objects.filter(in_office= True)
       

   

class EmployeeForm(forms.ModelForm): 
    
    class Meta:
        model = Employee
        exclude = ['in_office']
        widgets = {
            'title' : forms.Select(attrs = {'class': 'regDropDown'}),
            'name' : forms.TextInput(attrs = {'class': 'regDropDown'}),
            'designation' : forms.TextInput(attrs = {'class': 'regDropDown'}),
            'phone_no' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'department' : forms.Select(attrs={'class': 'regDropDown'}),
            'room_no' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class ExitForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['verification']
        widgets = {
            'verification' : forms.PasswordInput(attrs={'class':'form_control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['verification'].required = True
