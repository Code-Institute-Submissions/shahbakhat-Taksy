# Generated by Django 4.2.1 on 2023-06-14 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_mytrips_booking_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxi',
            old_name='booking_made_time',
            new_name='pickup_time',
        ),
    ]
