from django import forms
from django.contrib.auth.models import User
from myApp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class signupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password', 'email' ]
