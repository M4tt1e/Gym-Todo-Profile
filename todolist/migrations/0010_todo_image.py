# Generated by Django 3.2.7 on 2022-02-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_todo_user_last_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, upload_to='todo_attachments'),
        ),
    ]