# Generated by Django 3.2.7 on 2022-02-09 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0002_todo_time_since_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='time_since_created',
        ),
        migrations.AddField(
            model_name='todo',
            name='usr',
            field=models.ForeignKey(default='mateusze', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='importance',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1),
        ),
    ]