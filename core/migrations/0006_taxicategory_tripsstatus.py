# Generated by Django 4.2.1 on 2023-05-29 10:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_passenger_stripe_card_last4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=225, unique=True)),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='TripsStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('number_of_passengers', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('booking in proccess', 'Booking in process'), ('arrived', 'arrived'), ('onboard', 'Passenger on board'), ('cancelled', 'Trip has been canceled'), ('complete', 'Trip has been completed')], default='booking in proccess', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.taxicategory')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.passenger')),
            ],
        ),
    ]
