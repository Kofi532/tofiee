# Generated by Django 4.2.3 on 2023-08-20 00:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tofiee', '0003_alter_member_availability_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='availability_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 20, 0, 37, 4, 256706), max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='availability_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 20, 0, 37, 4, 256706), max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 20, 0, 37, 4, 256706)),
        ),
        migrations.AlterField(
            model_name='member',
            name='period_number',
            field=models.FloatField(blank=True, default=0, max_length=100),
        ),
    ]
