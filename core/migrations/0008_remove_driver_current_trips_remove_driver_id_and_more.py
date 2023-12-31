# Generated by Django 4.2.1 on 2023-06-22 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_taxi_accepted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='current_trips',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='id',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='id',
        ),
        migrations.AlterField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='driver', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='passenger', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
