# Generated by Django 4.2.1 on 2023-06-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('TAXIPASSENGER', 'Taxi Passenger'), ('TAXIDRIVER', 'Taxi Driver')], default='OTHER', max_length=50),
        ),
    ]
