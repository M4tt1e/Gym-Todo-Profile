# Generated by Django 3.2.7 on 2022-02-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_alter_todo_user_last_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='todo_attachments'),
        ),
    ]
