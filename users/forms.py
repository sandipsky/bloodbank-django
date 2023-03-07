from django import forms
from django.contrib.auth.models import User
from .models import *


class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields=['bloodgroup','address','mobile','profile_pic']


