# Generated by Django 4.0.2 on 2022-02-09 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 9, 16, 11, 52, 628618)),
        ),
    ]