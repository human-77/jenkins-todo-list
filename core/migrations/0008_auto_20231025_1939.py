# Generated by Django 2.1.7 on 2023-10-25 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20231025_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 10, 25, 19, 39, 13, 843698)),
        ),
    ]
