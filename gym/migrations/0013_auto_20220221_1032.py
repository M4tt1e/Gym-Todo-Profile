# Generated by Django 3.2.7 on 2022-02-21 10:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0012_auto_20220221_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='usr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 21, 10, 32, 54, 641647, tzinfo=utc), null=True),
        ),
    ]
