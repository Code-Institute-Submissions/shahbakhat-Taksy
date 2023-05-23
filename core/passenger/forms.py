from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from core.models import Passenger

class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('profile_photo', 'phone_number' )
