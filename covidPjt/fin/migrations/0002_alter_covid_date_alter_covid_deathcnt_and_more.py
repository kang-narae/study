# Generated by Django 4.0.2 on 2022-02-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='date',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='covid',
            name='deathCnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='covid',
            name='decideCnt',
            field=models.IntegerField(default=0),
        ),
    ]