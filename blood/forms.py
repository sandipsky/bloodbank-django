from django import forms
from .models import *


class BloodForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['bloodgroup','unit','status']

class RequestForm(forms.ModelForm):
    class Meta:
        model=BloodRequest
        fields=['reason','bloodgroup','unit']
