# Generated by Django 4.2.1 on 2023-06-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_passenger_profile_photo_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='stripe_card_last4',
        ),
        migrations.RemoveField(
            model_name='taxi',
            name='taxi_passneger_payment_method',
        ),
        migrations.AddField(
            model_name='taxi',
            name='trip_distance_covered',
            field=models.CharField(default=None, max_length=255,null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='dropoff_lat',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='dropoff_lng',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='pickup_lat',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='pickup_lng',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='taxi_booking_status',
            field=models.CharField(choices=[('booking in progress', 'Booking in progress'), ('arrived', 'Arrived'), ('booked', 'Booked'), ('onboard', 'Onboard'), ('cancelled', 'Cancelled'), ('complete', 'Completed')], max_length=100),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='taxi_size',
            field=models.CharField(choices=[('5 Seater', '5 Seater'), ('7 Seater', '7 Seater'), ('8 Seater', '8 Seater')], default='5 Seater', max_length=10),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='trip_distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]