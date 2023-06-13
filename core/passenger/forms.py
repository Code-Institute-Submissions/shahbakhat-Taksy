from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from core.models import Passenger,Taxi
# from django.forms import ModelForm


class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('profile_photo', 'phone_number')

class TaxiBookingForm(forms.ModelForm):
    pickup_address = forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Where are you?',
            # 'id': 'pickup-address-input',
        })
    )
    dropoff_address = forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Where do you want to go?',
            # 'id': 'dropoff-address-input',
        })
    )
    description = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': 'Write description or a message for Driver'}),
    required=False
)

    # distance = forms.CharField(required=False ,)


    class Meta:
        model = Taxi
        fields = ('pickup_address', 'pickup_lng', 'pickup_lat', 'dropoff_address','dropoff_lng', 'dropoff_lat', 'taxi_size','description')




