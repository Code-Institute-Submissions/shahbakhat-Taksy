# Generated by Django 4.2.1 on 2023-06-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_passenger_stripe_card_last4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxi',
            name='description',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='trip_distance_covered',
            field=models.CharField(blank=True, default='', max_length=255,null=True),
        ),
    ]
