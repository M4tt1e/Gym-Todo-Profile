# Generated by Django 3.2.7 on 2022-02-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time_since_created',
            field=models.DurationField(default=0),
        ),
    ]
