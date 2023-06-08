from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
import uuid
from django.utils import timezone


# Create your models here.
class Passenger(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='passenger/pfoile-photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True)
    stripe_customer_id = models.CharField(max_length=225, blank=True)
    stripe_payment_method_id= models.CharField(max_length=225, blank=True)
    stripe_card_last4 = models.CharField(max_length=225, blank=True)
    def __str__(self):
        return self.user.get_full_name()

# Taxi models
class Taxi (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable= False)
    slug = models.SlugField(max_length=255, unique=True)
    taxi_passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=False)
    FIVE_SEATER = "5 Seater"
    SEVEN_SEATER = "7 Seater"
    EIGHT_SEATER = "7 Seater"
    TAXI_SIZE = (
        (FIVE_SEATER ,'5 Seater'),
        (SEVEN_SEATER ,' 7 Seater'),
        (EIGHT_SEATER ,' 8 Seater'),
    )
    # Booking Statusses
    BOOKING_IN_PROGRESS = 'booking in proccess'
    BOOKING_STATUS = 'booked'
    TAXI_ARRIVED = 'arrived'
    PASSENGER_ONBOAD = 'onboard'
    TRIP_COMPLETED = 'complete'
    TRIP_CANCELLED = 'cancelled'
    STATUSES = (
        (BOOKING_IN_PROGRESS,'Booking in process'),
        (TAXI_ARRIVED,'Arrived'),
        (BOOKING_STATUS , 'Booked'),
        (PASSENGER_ONBOAD , 'You are on board'),
        (TRIP_CANCELLED , 'Trip has been canceled'),
        (TRIP_COMPLETED , 'Trip has been completed')

    )
    # Booking details
    taxi_size =models.CharField(max_length=10,choices=TAXI_SIZE, default=FIVE_SEATER)
    pickup_address = models.CharField(max_length=255, blank=False, default=None)
    dropoff_address = models.CharField(max_length=255, blank=False, default=None)
    pickup_lng = models.FloatField(default=0.0)
    pickup_lat = models.FloatField(default=0.0)
    dropoff_lng = models.FloatField(default=0.0)
    dropoff_lat = models.FloatField(default=0.0)
    trip_price = models.FloatField(default=0)
    taxi_booking_status = models.CharField(max_length=100, choices=STATUSES, default=BOOKING_IN_PROGRESS)
    # payment_option = models.CharField(choices=PAYMENT_CHOICES, max_length=2,)

    def __str__(self):
            return self.taxi_passenger


