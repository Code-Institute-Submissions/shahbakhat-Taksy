# Generated by Django 4.2.1 on 2023-06-02 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_user_passenegr_taxi_taxi_passenger_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='passenger',
            new_name='user',
        ),
    ]
