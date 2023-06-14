from django import forms
from django.contrib.auth.models import User
from core.models import Passenger, Taxi
from tempus_dominus.widgets import DateTimePicker


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
        })
    )
    dropoff_address = forms.CharField(
        max_length=255,
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Where do you want to go?',
        })
    )
    taxi_size = forms.ChoiceField(
        choices=Taxi.TAXI_SIZE,
        label='',
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': 'Write description or a message for the driver'}),
        required=False
    )



    class Meta:
        model = Taxi
        fields = ('pickup_address', 'pickup_lng', 'pickup_lat', 'dropoff_address', 'pickup_time', 'dropoff_lng', 'dropoff_lat', 'taxi_size', 'description')
