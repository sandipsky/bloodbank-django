from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1', 'password2']

class DonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields=['name','bloodgroup','dob','location','email','mobile','disease']

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=['name','location','email','mobile','identification']



