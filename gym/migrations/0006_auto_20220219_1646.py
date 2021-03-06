# Generated by Django 3.2.7 on 2022-02-19 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_auto_20220219_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='reps',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gym.workout'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 19, 16, 45, 5, 379416, tzinfo=utc), null=True),
        ),
    ]
