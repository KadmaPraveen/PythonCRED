#from dataclasses import fields
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
  #here tha fields used display name style change inhtml if u change below order html view order also change
     class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

        #add this line for select option in dropdown
        #give inline data is too importent
     def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False