# Generated by Django 3.2.7 on 2022-02-19 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20220219_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reps',
            name='workout',
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 19, 16, 41, 58, 653093, tzinfo=utc), null=True),
        ),
    ]
