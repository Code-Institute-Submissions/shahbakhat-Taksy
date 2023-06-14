from django import forms
from django.contrib.auth.models import User
from core.models import Passenger, Taxi
from django.forms import DateInput, TimeInput


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
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': 'Write description or a message for the driver'}),
        required=False

    )
    pickup_date = forms.DateField(
        label='Pickup Date',
        widget=DateInput(attrs={'type': 'date'})
    )
    pickup_time = forms.TimeField(
        label='Pickup Time',
        widget=TimeInput(attrs={'type': 'time'})
    )



    class Meta:
        model = Taxi
        fields = ('pickup_address', 'pickup_lng', 'pickup_lat', 'dropoff_address','pickup_time','pickup_date', 'dropoff_lng', 'dropoff_lat', 'taxi_size', 'description')
