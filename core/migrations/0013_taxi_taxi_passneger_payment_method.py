# Generated by Django 4.2.1 on 2023-06-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_taxi_taxi_passenger_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxi',
            name='taxi_passneger_payment_method',
            field=models.CharField(default='', max_length=50),
        ),
    ]