# Generated by Django 3.2.13 on 2022-06-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airMonitor', '0003_auto_20220614_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bme280reading',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='dht22reading',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sds011reading',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
