# Generated by Django 4.0.2 on 2022-02-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('date', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('deathCnt', models.CharField(default=0, max_length=100)),
                ('decideCnt', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]
