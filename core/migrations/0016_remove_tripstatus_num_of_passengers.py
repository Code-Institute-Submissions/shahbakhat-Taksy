# Generated by Django 4.2.1 on 2023-05-29 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_tripstatus_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripstatus',
            name='num_of_passengers',
        ),
    ]
