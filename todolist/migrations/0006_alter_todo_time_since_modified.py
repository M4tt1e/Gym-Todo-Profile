# Generated by Django 3.2.7 on 2022-02-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20220213_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time_since_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
